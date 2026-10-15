import { conversationalSearch } from "./conversational_search";

async function main() {
  const userId = process.argv[2];
  const message = process.argv.slice(3).join(" ");

  if (!userId || !message) {
    console.error(
      'Usage: run_conversation.ts <userId> "<message>"'
    );
    process.exit(1);
  }

  try {
    const result = await conversationalSearch(userId, message);
    console.log(result.message);
  } catch (error) {
    console.error("Property search failed:", error);
    process.exit(1);
  }
}

main();
