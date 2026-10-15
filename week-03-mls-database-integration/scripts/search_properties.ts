import { parsePropertyQuery } from "./parse_property_query";
import { searchActiveListings } from "./active_listings";

export async function searchProperties(userQuery: string) {
	const filters = await parsePropertyQuery(userQuery);
	return searchActiveListings(filters);
}
