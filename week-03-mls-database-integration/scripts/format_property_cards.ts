type PropertyRow = Record<string, any>;

export function formatPropertyCards(properties: PropertyRow[]): string {
  if (properties.length === 0) {
    return "No properties found.";
  }

  return properties
    .map((property, index) => {
      return [
        `Property ${index + 1}`,
        `Address: ${property.L_Address}, ${property.L_City}, ${property.L_Zip}`,
        `Price: $${Number(property.price).toLocaleString("en-US")}`,
        `Beds: ${property.beds}`,
        `Baths: ${property.baths}`,
        `Square Feet: ${property.sqft}`,
        `Type: ${property.type}`,
        `Status: ${property.status}`,
      ].join("\n");
    })
    .join("\n\n");
}
