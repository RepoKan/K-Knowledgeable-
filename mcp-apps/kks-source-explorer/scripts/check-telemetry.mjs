// Isolated pilot: require explicit CLI telemetry opt-out before development commands.
const enabled = process.env.SKYBRIDGE_TELEMETRY_DISABLED === '1' && process.env.DO_NOT_TRACK === '1';
if (!enabled) {
  console.error('BLOCKED: set SKYBRIDGE_TELEMETRY_DISABLED=1 and DO_NOT_TRACK=1 before Skybridge commands.');
  process.exitCode = 2;
}
