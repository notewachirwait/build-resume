// Accepts an array of order ID strings, returns only IDs that appear more than once
function findDuplicateOrders(orderIds: string[]): string[] {

    // Create a Map to track how many times each ID appears: { "o1" -> 2, "o2" -> 1, ... }
    const count = new Map<string, number>();

    // Loop through every order ID in the input array
    for (const id of orderIds) {
        // If ID exists in map → get current count. If not → default to 0. Then add 1.
        count.set(id, (count.get(id) ?? 0) + 1);
    }

    // Spread all [id, count] pairs from the Map into an array
    return [...count.entries()]
        // Keep only entries where count > 1 (appeared more than once)
        .filter(([, n]) => n > 1)
        // Extract just the ID string, discard the count number
        .map(([id]) => id);
}

// Tests
describe('findDuplicateOrders', () => {
    test('returns duplicates', () => {
        const result = findDuplicateOrders(['o1', 'o2', 'o3', 'o1', 'o4', 'o2', 'o5', 'o3']);
        expect(result.sort()).toEqual(['o1', 'o2', 'o3']);
    });

    test('returns empty when no duplicates', () => {
        expect(findDuplicateOrders(['o1', 'o2',])).toEqual([]);
    });

    test('returns empty for empty input', () => {
        expect(findDuplicateOrders([])).toEqual([]);
    });
});
