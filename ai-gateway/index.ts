import { generateText } from 'ai';

async function main() {
  if (!process.env.AI_GATEWAY_API_KEY?.trim()) {
    console.error('Enter AI_GATEWAY_API_KEY locally in .env.local, then run npm start.');
    process.exitCode = 1;
    return;
  }

  try {
    const { text } = await generateText({
      model: 'moonshotai/kimi-k3',
      prompt: 'Invent a new holiday and describe its traditions.',
      abortSignal: AbortSignal.timeout(60_000),
      maxRetries: 0,
    });

    if (!text.trim()) {
      console.error('AI Gateway returned no text.');
      process.exitCode = 1;
      return;
    }

    console.log(text);
  } catch {
    // Keep SDK errors private: they can contain request or credential details.
    console.error('Generation failed. Check the local key, model access, account credits, and network connection.');
    process.exitCode = 1;
  }
}

await main();
