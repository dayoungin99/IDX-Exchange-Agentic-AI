import { getSession } from "./session";

export function getFollowUpQuestion(userId: string): string | null {
  const session = getSession(userId);

  if (!session.city) {
    return "Which city are you interested in?";
  }

  if (session.maxPrice === undefined) {
    return "What is your budget?";
  }

  if (session.type === undefined) {
    return "What type of property are you looking for?";
  }

  if (session.beds === undefined) {
    return "How many bedrooms do you need?";
  }

  return null;
}
