import { parsePropertyQuery } from "./parse_property_query";

const tests = [
  {
    query: "Show me 3-bedroom condos in Irvine under $1.5M with a pool.",
    expected: {
      city: "Irvine",
      maxPrice: 1500000,
      beds: 3,
      type: "Condominium",
      pool: "True",
    },
  },
  {
    query: "Find 2-bedroom condos in Newport Beach under $900k.",
    expected: {
      city: "Newport Beach",
      maxPrice: 900000,
      beds: 2,
      type: "Condominium",
    },
  },
  {
    query: "Show me 4-bedroom single family homes in Anaheim under $2M.",
    expected: {
      city: "Anaheim",
      maxPrice: 2000000,
      beds: 4,
      type: "SingleFamilyResidence",
    },
  },
  {
    query: "Find townhome in Costa Mesa under $800k with a pool.",
    expected: {
      city: "Costa Mesa",
      maxPrice: 800000,
      type: "Townhouse",
      pool: "True",
    },
  },
  {
    query: "Show me land in Laguna Beach under $3M with a view.",
    expected: {
      city: "Laguna Beach",
      maxPrice: 3000000,
      type: "UnimprovedLand",
      hasView: "True",
    },
  },
  {
    query: "Find 3-bedroom homes in Tustin with a pool.",
    expected: {
      city: "Tustin",
      beds: 3,
      pool: "True",
    },
  },
  {
    query: "Show me condos in Fullerton under $750,000.",
    expected: {
      city: "Fullerton",
      maxPrice: 750000,
      type: "Condominium",
    },
  },
  {
    query: "Find 2.5 bath condos in Irvine under $1M.",
    expected: {
      city: "Irvine",
      maxPrice: 1000000,
      baths: 2.5,
      type: "Condominium",
    },
  },
  {
    query: "Show me 2000 sq ft townhome in Orange under $1.2M.",
    expected: {
      city: "Orange",
      maxPrice: 1200000,
      sqft: 2000,
      type: "Townhouse",
    },
  },
  {
    query: "Find 4-bedroom condos in Santa Ana with a view and HOA under $500.",
    expected: {
      city: "Santa Ana",
      beds: 4,
      type: "Condominium",
      hasView: "True",
      maxHoa: 500,
    },
  },
];

async function main() {
  for (let i = 0; i < tests.length; i++) {
    const { query, expected } = tests[i];
    const result = await parsePropertyQuery(query);

    const passed = Object.entries(expected).every(
      ([key, value]) => result[key as keyof typeof result] === value
    );

    console.log(`Test ${i + 1}: ${passed ? "PASS" : "FAIL"}`);

    if (!passed) {
      console.log("Query:", query);
      console.log("Expected:", expected);
      console.log("Received:", result);
    }
  }
}

main();
