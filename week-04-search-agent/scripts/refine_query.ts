import { parsePropertyQuery } from "./parse_property_query";
import { getSession, updateSession } from "./session";

export async function refineQuery(userId: string, message: string) {
  const newFilters = await parsePropertyQuery(message);

  const updates = Object.fromEntries(
    Object.entries(newFilters).filter(
      ([, value]) => value !== undefined && value !== null
    )
  );

  updateSession(userId, updates);

  return getSession(userId);
}
