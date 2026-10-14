import { Skybridge } from 'skybridge/server';
import { z } from 'zod';
import { listReferenceSources, getIntegrationStatus } from './data/reference-fixture.mjs';

const readOnly = { readOnlyHint: true, openWorldHint: false, destructiveHint: false } as const;
export const app = new Skybridge({
  name: 'kks-source-explorer',
  version: '0.1.0',
  handler: (server) => server
    .registerTool({
      name: 'list_reference_sources',
      description: 'List public allowlisted KKS and Skybridge sources with provenance. Dated snapshot, not live GitHub.',
      inputSchema: { category: z.enum(['all', 'framework', 'governance', 'integration']).optional() },
      annotations: readOnly,
      view: {
        component: 'reference-sources',
        description: 'Browsable public source list and provenance.',
        csp: { redirectDomains: ['https://github.com', 'https://docs.skybridge.tech'] },
      },
    }, async (input) => {
      const structuredContent = listReferenceSources(input);
      return {
        structuredContent,
        content: [{ type: 'text', text: JSON.stringify(structuredContent) }],
      };
    })
    .registerTool({
      name: 'get_integration_status',
      description: 'Report KKS MCP candidate status and verification gaps from offline fixture. Not live CI.',
      inputSchema: {},
      annotations: readOnly,
      view: {
        component: 'integration-status',
        description: 'Candidate integration checks and blockers.',
      },
    }, async (input) => {
      const structuredContent = getIntegrationStatus(input);
      return {
        structuredContent,
        content: [{ type: 'text', text: JSON.stringify(structuredContent) }],
      };
    }),
});
export type AppType = typeof app;
