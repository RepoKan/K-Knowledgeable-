import assert from 'node:assert/strict';
import http from 'node:http';

process.env.NODE_ENV = 'production';
process.env.VERCEL = '1'; // select the local Express adapter, not a deployment
process.env.SKYBRIDGE_TELEMETRY_DISABLED = '1';
process.env.DO_NOT_TRACK = '1';
process.env.ALPIC_API_BASE_URL = 'http://127.0.0.1:9';
const { default: app } = await import('../dist/__entry.js');
const server = http.createServer(app);
await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
const base = `http://127.0.0.1:${server.address().port}`;
let id = 0;
async function rpc(method, params) {
  const response = await fetch(base + '/mcp', {
    method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json, text/event-stream' },
    body: JSON.stringify({ jsonrpc: '2.0', id: ++id, method, params }), signal: AbortSignal.timeout(5000),
  });
  const text = await response.text();
  const event = text.split('\n').find(line => line.startsWith('data:'));
  return JSON.parse(event ? event.slice(5) : text);
}
try {
  for (const path of ['/__skybridge/deploy/status', '/__skybridge/deploy/login', '/__skybridge/tunnel', '/__skybridge/tunnel/events']) {
    for (const method of ['GET', 'POST']) {
      const response = await fetch(base + path, { method, signal: AbortSignal.timeout(5000) });
      assert.equal(response.status, 403, `${method} ${path} must fail closed`);
    }
  }
  const initialized = await rpc('initialize', { protocolVersion: '2025-03-26', capabilities: {}, clientInfo: { name: 'fixture-runtime-test', version: '1.0' } });
  assert.equal(initialized.result.serverInfo.name, 'kks-source-explorer');
  const listed = await rpc('tools/list', {});
  assert.deepEqual(listed.result.tools.map(tool => tool.name).sort(), ['get_integration_status', 'list_reference_sources']);
  const sources = await rpc('tools/call', { name: 'list_reference_sources', arguments: { category: 'all' } });
  assert.ok(sources.result.structuredContent.sources.length > 0);
  assert.ok(sources.result.content.some(part => part.type === 'text'));
  const status = await rpc('tools/call', { name: 'get_integration_status', arguments: {} });
  assert.equal(status.result.structuredContent.status, 'CANDIDATE');
  const rejected = await rpc('tools/call', { name: 'list_reference_sources', arguments: { category: 'https://untrusted.invalid' } });
  assert.ok(rejected.error || rejected.result?.isError);
  console.log('PASS: actual built MCP initialize/list/calls/input rejection and 8 cloud/tunnel denial checks; loopback only');
} finally {
  server.closeAllConnections();
  await new Promise(resolve => server.close(resolve));
}
