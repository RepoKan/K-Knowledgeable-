# AI Gateway holiday example

Requires Node.js 24 or newer and npm.

```sh
npm ci
```

Open `.env.local` in your local editor and set `AI_GATEWAY_API_KEY` to your
Vercel AI Gateway key. If the file is missing, create it with that variable.
Enter the key only in the file, never in chat or a shell command. Git ignores
`.env.local`; do not force-add or commit it.

```sh
npm start
```

The command loads `.env.local` using Node's built-in environment file support
and runs `index.ts` using Node's built-in TypeScript support. It calls
`generateText` from `ai` with `moonshotai/kimi-k3` and prints the generated
holiday and traditions. Empty responses and failed requests exit with code 1.
SDK error objects are not logged.

Live generation is unverified until the example exits successfully and prints
nonempty generated text with a locally configured key.

## Vercel deployment configuration matrix

This package is a separate Node.js service. The Python cooking-agent directory
is not its deployment root. Upload these source files to the intended Git
repository; local workspace edits are not automatically pushed to GitHub.

| Step | Setting | Value |
| --- | --- | --- |
| 1 | Root Directory | Directory containing this package.json, api/, and vercel.json |
| 2 | Framework Preset | Other |
| 3 | Node.js Version | 24.x |
| 4 | Install Command | npm ci |
| 5 | Build Command | Leave unset; do not use npm start as a build command |
| 6 | Output Directory | public (configured in vercel.json) |
| 7 | Environment variable name | AI_GATEWAY_API_KEY |
| 8 | Environment variable value | Enter a replacement key directly in Vercel |
| 9 | Environment targets | Production; Preview when needed |
| 10 | Deployment Protection | Keep enabled while testing this paid inference endpoint |
| 11 | Validation | npm run check, then npm test |
| 12 | Deploy | Deploy the commit containing this service |
| 13 | HTTP test | Send POST /api through an authorized session |

Vercel loads api/index.ts as a Node.js function. It returns JSON containing
`text` on successful generation; GET returns 405, missing credentials return
503, and provider failures or empty text return 502. Responses are not cached.
The endpoint has a fixed prompt and does not accept arbitrary input.

The root URL serves public/index.html as a mobile-friendly browser preview.
Its button sends POST /api and shows either the generated holiday or the API
error. Static output is restricted to public/ so terminal TypeScript source
and configuration files are not served as downloadable website content.

The terminal command still uses index.ts. On Vercel, the function reads the
environment variable configured in the dashboard; do not upload .env.local.

## Verification status

- Local HTTP contract tests use the AI SDK's mock provider and make no network
  calls. Their success does not prove live model generation.
- Live requests previously returned HTTP 403 with a payment-method/credits
  requirement. Resolve this for the team owning the key before retesting.
- A deployed Vercel build and a successful live POST /api are still required
  before claiming deployment and Gateway integration work end to end.
