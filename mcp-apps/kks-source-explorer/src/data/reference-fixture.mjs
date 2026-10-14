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
    snapshot_at: SNAPSHOT_DATE,
    checks: [
      { name: 'SPEC_R1_APPROVAL', state: 'CONFIRMED', evidence: 'Read-only, fixture-only development approved by user on 2026-10-14.' },
      { name: 'UPSTREAM_SOURCE', state: 'CONFIRMED', evidence: `alpic-ai/skybridge@${FRAMEWORK_SHA}; third-party source reviewed 2026-10-14.` },
      { name: 'LOCKFILE_AND_NPM_INSTALL', state: 'NOT_RUN', evidence: 'Dependency lockfile and install not verified.' },
      { name: 'NODE24_SKYBRIDGE_RUNTIME', state: 'NOT_RUN', evidence: 'Actual MCP server execution not verified.' },
      { name: 'REACT_VIEW_IN_CLIENT', state: 'NOT_RUN', evidence: 'Client and React view rendering not verified.' },
      { name: 'EXACT_HEAD_CI', state: 'UNVERIFIED', evidence: 'Check live GitHub workflow for current head; this is an offline snapshot.' },
      { name: 'MERGE_OR_DEPLOY', state: 'NOT_APPROVED', evidence: 'No fresh merge/deployment approval.' },
    ],
    blockers: [
      'Install and audit locked dependencies on isolated Node >=24.18.0 with telemetry disabled.',
      'Verify real MCP initialize/tools/list/tool calls and React view.',
      'Verify latest head CI and obtain separate merge or deployment approval.',
    ],
    next_review_action: 'Run isolated runtime, protocol, UI and egress checks; retain draft PR.',
  };
}
