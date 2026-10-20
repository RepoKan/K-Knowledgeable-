import assert from 'node:assert/strict';
import { spawn } from 'node:child_process';
import { mkdtemp, mkdir, readFile, rm, writeFile } from 'node:fs/promises';
import { createRequire } from 'node:module';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { setTimeout as delay } from 'node:timers/promises';
import test from 'node:test';

test('nodemon with the Chokidar override restarts for fixture changes', { timeout: 20000 }, async () => {
  const root = await mkdtemp(path.join(tmpdir(), 'kks-watcher-'));
  const config = JSON.parse(await readFile(new URL('../nodemon.json', import.meta.url), 'utf8'));
  assert.deepEqual(config.watch, ['src']);
  assert.ok(config.ext.split(',').includes('mjs'));
  await mkdir(path.join(root, 'src'));
  await writeFile(path.join(root, 'probe.cjs'), "console.log('PROBE_READY'); setInterval(() => {}, 1000);\n");
  await writeFile(path.join(root, 'src', 'fixture.mjs'), 'export const value = 1;\n');
  const require = createRequire(import.meta.url);
  const child = spawn(process.execPath, [require.resolve('nodemon/bin/nodemon.js'), '--watch', 'src', '--ext', config.ext, '--exec', `${process.execPath} probe.cjs`], {
    cwd: root, stdio: ['ignore', 'pipe', 'pipe'], detached: process.platform !== 'win32',
  });
  let output = '';
  child.stdout.on('data', chunk => { output += chunk; });
  child.stderr.on('data', chunk => { output += chunk; });
  const waitForStarts = async count => {
    const deadline = Date.now() + 7000;
    while ((output.match(/PROBE_READY/g) || []).length < count) {
      if (Date.now() > deadline || child.exitCode !== null) assert.fail(output);
      await delay(50);
    }
  };
  try {
    await waitForStarts(1);
    await delay(300); // let the initial recursive scan settle
    await writeFile(path.join(root, 'src', 'fixture.mjs'), 'export const value = 2;\n');
    await waitForStarts(2);
    await writeFile(path.join(root, 'src', 'new.ts'), 'export const value = 3;\n');
    await waitForStarts(3);
    await rm(path.join(root, 'src', 'new.ts'));
    await waitForStarts(4);
  } finally {
    if (child.exitCode === null) {
      const exited = new Promise(resolve => child.once('exit', resolve));
      if (process.platform !== 'win32') process.kill(-child.pid, 'SIGTERM');
      else child.kill('SIGTERM');
      await exited;
    }
    child.stdout.destroy();
    child.stderr.destroy();
    await rm(root, { recursive: true, force: true });
  }
});
