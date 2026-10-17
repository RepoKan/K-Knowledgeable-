import assert from 'node:assert/strict';
import { existsSync } from 'node:fs';
import test from 'node:test';
import { MockLanguageModelV4, MockProviderV4 } from 'ai/test';

test('HTTP API handles methods, missing credentials, generation, and provider failures', async () => {
  assert.ok(existsSync(new URL('../api/index.ts', import.meta.url)), 'Deployable API entrypoint must exist');
  const { default: api } = await import('../api/index.ts');

  const get = await api.fetch(new Request('https://example.test/api'));
  assert.equal(get.status, 405);
  assert.equal(get.headers.get('allow'), 'POST');

  delete process.env.AI_GATEWAY_API_KEY;
  const missing = await api.fetch(new Request('https://example.test/api', { method: 'POST' }));
  assert.equal(missing.status, 503);

  process.env.AI_GATEWAY_API_KEY = 'test-only-placeholder';
  const model = new MockLanguageModelV4({
    doGenerate: {
      content: [{ type: 'text', text: 'Lantern Day celebrates kindness with homemade lanterns.' }],
      finishReason: { unified: 'stop', raw: 'stop' },
      usage: {
        inputTokens: { total: 10, noCache: 10, cacheRead: 0, cacheWrite: 0 },
        outputTokens: { total: 12, text: 12, reasoning: 0 },
      },
      warnings: [],
    },
  });
  globalThis.AI_SDK_DEFAULT_PROVIDER = new MockProviderV4({
    languageModels: { 'moonshotai/kimi-k3': model },
  });
  try {
    const generated = await api.fetch(new Request('https://example.test/api', { method: 'POST' }));
    assert.equal(generated.status, 200);
    assert.match((await generated.json()).text, /Lantern Day/);
    assert.equal(generated.headers.get('cache-control'), 'no-store');

    model.doGenerate = async () => { throw new Error('sensitive-provider-diagnostic'); };
    const failed = await api.fetch(new Request('https://example.test/api', { method: 'POST' }));
    assert.equal(failed.status, 502);
    assert.doesNotMatch(await failed.text(), /sensitive-provider-diagnostic|test-only-placeholder/);
  } finally {
    delete process.env.AI_GATEWAY_API_KEY;
    delete globalThis.AI_SDK_DEFAULT_PROVIDER;
  }
});
