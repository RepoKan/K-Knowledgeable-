import { existsSync, readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const [major, minor] = process.versions.node.split('.').map(Number);
function block(reason) { console.error('BLOCKED: ' + reason); process.exitCode = 2; }
if (major < 24 || (major === 24 && minor < 18)) {
  block('Node >=24.18.0 is required; use an isolated runtime.');
} else if (process.env.SKYBRIDGE_TELEMETRY_DISABLED !== '1' || process.env.DO_NOT_TRACK !== '1') {
  block('Set SKYBRIDGE_TELEMETRY_DISABLED=1 and DO_NOT_TRACK=1.');
} else if (!existsSync(path.join(root, 'package-lock.json'))) {
  block('A genuine reviewed npm package-lock.json is required.');
} else {
  const pkg = JSON.parse(readFileSync(path.join(root, 'package.json'), 'utf8'));
  const lock = JSON.parse(readFileSync(path.join(root, 'package-lock.json'), 'utf8'));
  if (lock.lockfileVersion < 3 || lock.packages?.['']?.name !== pkg.name) {
    block('Lockfile is invalid or does not match this project.');
  } else {
    console.log('PASS: static startup preflight. Runtime and egress are not yet verified.');
  }
}
