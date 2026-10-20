import '../index.css';
import { useToolInfo } from '../helpers.js';

export default function IntegrationStatus() {
  const { output, isPending } = useToolInfo<'get_integration_status'>();
  if (isPending || !output) return <section className="panel" role="status">Loading candidate status…</section>;
  return <section className="panel" aria-labelledby="status-title">
    <div className="panel-head"><h2 id="status-title">KKS integration status</h2><span className="state">{output.status}</span></div>
    <p className="muted">Snapshot {output.snapshot_at}. Not live CI or Production state.</p>
    <ul className="check-list">{output.checks.map(check => <li key={check.name}>
      <div className="source-row"><strong>{check.name.replaceAll('_', ' ')}</strong><span className="tag">{check.state}</span></div>
      <p>{check.evidence}</p>
    </li>)}</ul>
    <h3>Outstanding gates</h3>
    <ul className="blockers">{output.blockers.map(item => <li key={item}>{item}</li>)}</ul>
    <p className="footnote">{output.next_review_action}</p>
  </section>;
}
