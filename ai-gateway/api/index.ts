import { generateText } from 'ai';

export default {
  async fetch(request: Request): Promise<Response> {
    const headers = { 'Cache-Control': 'no-store' };

    if (request.method !== 'POST') {
      return Response.json(
        { error: 'Use POST /api to generate a holiday.' },
        { status: 405, headers: { ...headers, Allow: 'POST' } },
      );
    }

    if (!process.env.AI_GATEWAY_API_KEY?.trim()) {
      return Response.json(
        { error: 'AI Gateway is not configured.' },
        { status: 503, headers },
      );
    }

    try {
      const { text } = await generateText({
        model: 'moonshotai/kimi-k3',
        prompt: 'Invent a new holiday and describe its traditions.',
        abortSignal: AbortSignal.timeout(45_000),
        maxRetries: 0,
      });

      if (!text.trim()) {
        return Response.json({ error: 'AI Gateway returned no text.' }, { status: 502, headers });
      }

      return Response.json({ text }, { headers });
    } catch {
      // Do not expose provider error objects or request credentials.
      return Response.json(
        { error: 'Generation failed. Check Gateway billing, model access, and credentials.' },
        { status: 502, headers },
      );
    }
  },
};
