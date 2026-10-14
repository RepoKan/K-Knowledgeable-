import { strict as assert } from 'node:assert';
import test from 'node:test';
import { listReferenceSources, getIntegrationStatus, CATEGORIES, FRAMEWORK_SHA, KKS_BASE_SHA } from '../src/data/reference-fixture.mjs';

const urls = listReferenceSources().sources.map(s => s.url);

test('sources are allowlisted HTTPS with no embedded authentication', () => {
  assert.equal(urls.length, 5);
  assert.equal(new Set(urls).size, 5);
  for (const url of urls) {
    const parsed = new URL(url);
    assert.equal(parsed.protocol, 'https:');
    assert.ok(['github.com', 'docs.skybridge.tech'].includes(parsed.hostname));
    assert.equal(parsed.username, '');
    assert.equal(parsed.password, '');
    assert.equal(parsed.search, '');
  }
});
test('sources have traceable revisions', () => {
  assert.equal(FRAMEWORK_SHA.length, 40);
  assert.equal(KKS_BASE_SHA.length, 40);
  assert.ok(urls.some(url => url.includes(FRAMEWORK_SHA)));
});
test('all categories partition the sources', () => {
  const groups = CATEGORIES.filter(category => category !== 'all')
    .flatMap(category => listReferenceSources({category}).sources);
  assert.deepEqual(groups.map(s => s.id).sort(), listReferenceSources().sources.map(s => s.id).sort());
});
test('default category is all', () => {
  assert.deepEqual(listReferenceSources({}), listReferenceSources());
});
test('source output is explicitly a snapshot', () => {
  assert.equal(listReferenceSources().evidence_state, 'PUBLIC_SNAPSHOT_ONLY');
});
test('no URL or arbitrary path parameter', () => {
  for (const value of [{url:'https://invalid'}, {path:'/etc/passwd'}, {repo:'private'}, {category:'all', query:'x'}]) {
    assert.throws(() => listReferenceSources(value), TypeError);
  }
});
test('reject unknown and malformed categories', () => {
  for (const category of ['private', '../', '', 'ALL', null, 123, ['all']]) {
    assert.throws(() => listReferenceSources({category}), RangeError);
  }
});
test('reject array/null/primitive inputs', () => {
  for (const value of [null, [], 'all', 12]) {
    assert.throws(() => listReferenceSources(value), TypeError);
    assert.throws(() => getIntegrationStatus(value), TypeError);
  }
});
test('source output is cloned', () => {
  const result = listReferenceSources();
  result.sources[0].title = 'changed';
  result.sources.push({url:'https://invalid'});
  assert.notEqual(listReferenceSources().sources[0].title, 'changed');
  assert.equal(listReferenceSources().sources.length, urls.length);
});
test('status refuses arbitrary input and never claims live readiness', () => {
  assert.throws(() => getIntegrationStatus({refresh:true}), TypeError);
  const status = getIntegrationStatus();
  assert.equal(status.status, 'CANDIDATE');
  assert.equal(status.reviewed_head_sha, null);
  for (const state of ['NOT_RUN', 'NOT_APPROVED', 'UNVERIFIED']) {
    assert.ok(status.checks.some(check => check.state === state));
  }
});
test('public source records have no unsafe URL scheme', () => {
  assert.ok(urls.every(url => url.startsWith('https://')));
});
