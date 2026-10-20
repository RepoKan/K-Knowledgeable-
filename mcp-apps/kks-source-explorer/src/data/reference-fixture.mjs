/** Public allowlisted snapshots only. No network access and no arbitrary input URLs. */
export const FRAMEWORK_SHA = '6dd443908113b5218d20a5016ed6c34d223e5146';
export const KKS_BASE_SHA = '22406760ae8653003819141186d68d0a368e08b2';
export const SNAPSHOT_DATE = '2026-10-14';
export const CATEGORIES = Object.freeze(['all', 'framework', 'governance', 'integration']);

const SOURCES = Object.freeze([
  Object.freeze({
    id: 'skybridge-framework',
    title: 'Skybridge framework (upstream)',
    url: `https://github.com/alpic-ai/skybridge/tree/${FRAMEWORK_SHA}`,
    category: 'framework',
    authority: 'external upstream implementation',
    provenance: `alpic-ai/skybridge@${FRAMEWORK_SHA}`,
    verified_at: SNAPSHOT_DATE,
  }),
  Object.freeze({
    id: 'skybridge-quickstart',
    title: 'Skybridge quickstart (pinned source)',
    url: `https://github.com/alpic-ai/skybridge/blob/${FRAMEWORK_SHA}/docs/get-started/quickstart.mdx`,
    category: 'framework',
    authority: 'external upstream documentation',
    provenance: `alpic-ai/skybridge@${FRAMEWORK_SHA}`,
    verified_at: SNAPSHOT_DATE,
  }),
  Object.freeze({
    id: 'skybridge-docs',
    title: 'Skybridge documentation (moving website)',
    url: 'https://docs.skybridge.tech/',
    category: 'framework',
    authority: 'external official documentation, unpinned website',
    provenance: 'docs.skybridge.tech; contents may change',
    verified_at: SNAPSHOT_DATE,
  }),
  Object.freeze({
    id: 'kks-pr34',
    title: 'KKS Skybridge review draft (PR #34)',
    url: 'https://github.com/RepoKan/K-Knowledgeable-/pull/34',
    category: 'integration',
    authority: 'sanitized KKS candidate, not Production approval',
    provenance: `RepoKan/K-Knowledgeable-; base ${KKS_BASE_SHA}`,
    verified_at: SNAPSHOT_DATE,
  }),
  Object.freeze({
    id: 'kks-public-governance',
    title: 'KKS public Project instructions',
    url: `https://github.com/RepoKan/K-Knowledgeable-/blob/${KKS_BASE_SHA}/activation/PROJECT_INSTRUCTIONS.md`,
    category: 'governance',
    authority: 'sanitized project governance, not Production evidence',
    provenance: `RepoKan/K-Knowledgeable-@${KKS_BASE_SHA}`,
    verified_at: SNAPSHOT_DATE,
  }),
]);

function validateInput(input, fields) {
  if (input === null || typeof input !== 'object' || Array.isArray(input)
      || (Object.getPrototypeOf(input) !== Object.prototype
      && Object.getPrototypeOf(input) !== null)) {
    throw new TypeError('Expected a plain object input');
  }
  if (Object.keys(input).some(key => !fields.includes(key))) {
    throw new TypeError('Unexpected input field');
  }
}

export function listReferenceSources(input = {}) {
  validateInput(input, ['category']);
  const category = input.category === undefined ? 'all' : input.category;
  if (typeof category !== 'string' || !CATEGORIES.includes(category)) {
    throw new RangeError('Unsupported source category');
  }
  return {
    sources: SOURCES.filter(source => category === 'all' || source.category === category)
      .map(source => ({ ...source })),
    evidence_state: 'PUBLIC_SNAPSHOT_ONLY',
    snapshot_at: SNAPSHOT_DATE,
    note: 'Allowlisted public references only; this tool does not inspect live GitHub state.',
  };
}

export function getIntegrationStatus(input = {}) {
  validateInput(input, []);
  return {
    status: 'CANDIDATE',
    repository: 'RepoKan/K-Knowledgeable-',
    baseline_sha: KKS_BASE_SHA,
    reviewed_head_sha: null,
    snapshot_at: '2026-10-20',
    checks: [
      { name: 'SPEC_R1_APPROVAL', state: 'CONFIRMED', evidence: 'Read-only, fixture-only development approved by user on 2026-10-14.' },
      { name: 'UPSTREAM_SOURCE', state: 'CONFIRMED', evidence: `alpic-ai/skybridge@${FRAMEWORK_SHA}; third-party source reviewed 2026-10-14.` },
      { name: 'LOCKFILE_AND_NPM_INSTALL', state: 'CONFIRMED', evidence: 'Node 24.19.0: locked installation, watcher regression test and zero-vulnerability npm audit passed locally on 2026-10-20.' },
      { name: 'NODE24_SKYBRIDGE_RUNTIME', state: 'CONFIRMED', evidence: 'Actual loopback MCP initialize, tools/list, both calls and invalid-category rejection passed; cloud/tunnel routes return 403.' },
      { name: 'REACT_VIEW_IN_CLIENT', state: 'CONFIRMED', evidence: 'Both React views rendered in local DevTools on 2026-10-20. This is not a ChatGPT host-connection test.' },
      { name: 'EXACT_HEAD_CI', state: 'UNVERIFIED', evidence: 'Check live GitHub workflow for current head; this is an offline snapshot.' },
      { name: 'EXTERNAL_HOST_CONNECTION', state: 'NOT_RUN', evidence: 'No public tunnel or ChatGPT connector was registered.' },
      { name: 'MERGE_APPROVAL', state: 'CONFIRMED', evidence: 'Owner approved resolving and merging the reviewed outstanding PRs on 2026-10-20; this is not standing approval for future changes.' },
      { name: 'DEPLOYMENT', state: 'NOT_APPROVED', evidence: 'This pilot remains local-only; deployment and public connection require separate approval.' },
    ],
    blockers: [
      'Recheck exact-head CI and current dependency audit before any later change.',
      'Review separate authentication, host-connection and egress requirements before any public use.',
      'Obtain separate deployment and connector-registration approval; local tests do not grant it.',
    ],
    next_review_action: 'Verify the reviewed PR revision and CI in GitHub; retain CANDIDATE status for this local public-fixture pilot.',
  };
}
