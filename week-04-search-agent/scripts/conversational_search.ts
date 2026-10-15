import { formatPropertyCards } from "./format_property_cards";
import { refineQuery } from "./refine_query";
import { getFollowUpQuestion } from "./follow_up";
import { searchActiveListings } from "./active_listings";

export async function conversationalSearch(
  userId: string,
  message: string
) {
  const session = await refineQuery(userId, message);

  const followUp = getFollowUpQuestion(userId);

  if (followUp) {
    return {
      status: "needs_info",
      message: followUp,
      filters: session
    };
  }

  const listings = await searchActiveListings({
    city: session.city,
    maxPrice: session.maxPrice,
    beds: session.beds,
    baths: session.baths,
    type: session.type,
    pool: session.pool
  });

  return {
    status: "results",
    listings,
    message: formatPropertyCards(listings),
    filters: session
  };
}
