import '../index.css';
import { useState } from 'react';
import { useOpenExternal } from 'skybridge/web';
import { useToolInfo } from '../helpers.js';

type Filter = 'all' | 'framework' | 'governance' | 'integration';
const filters: Filter[] = ['all', 'framework', 'governance', 'integration'];

export default function ReferenceSources() {
  const { output, isPending } = useToolInfo<'list_reference_sources'>();
  const [filter, setFilter] = useState<Filter>('all');
  const openExternal = useOpenExternal();
  if (isPending || !output) return <section className="panel" role="status">Loading public references…</section>;
  const sources = output.sources.filter(source => filter === 'all' || source.category === filter);
  return <section className="panel" aria-labelledby="sources-title">
    <div className="panel-head">
      <h2 id="sources-title">KKS Source Explorer</h2>
      <span className="state">Public snapshot</span>
    </div>
    <p className="muted">Reviewed {output.snapshot_at}. External links only, not live repository queries.</p>
    <div className="filters" role="group" aria-label="Filter references">
      {filters.map(category => <button key={category} type="button"
        aria-pressed={filter === category} className={filter === category ? 'selected' : ''}
        onClick={() => setFilter(category)}>{category}</button>)}
    </div>
    <ul className="source-list">
      {sources.map(source => <li key={source.id}>
        <div className="source-row"><strong>{source.title}</strong><span className="tag">{source.category}</span></div>
        <p className="muted">{source.authority}</p>
        <details><summary>Provenance</summary><p>{source.provenance}</p></details>
        <button type="button" className="link-action"
          onClick={() => openExternal(source.url, { redirectUrl: false })}
          aria-label={`Open external public source: ${source.title}`}>Open public source</button>
      </li>)}
    </ul>
    <p className="footnote">{output.note}</p>
  </section>;
}
