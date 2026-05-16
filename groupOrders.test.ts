// ─── Types ────────────────────────────────────────────────────────────────────

// Each order has an id (string) and a status (string like 'pending', 'delivered', etc.)
interface Order {
    id: string;
    status: string;
}

// Result type: keys are status strings, values are arrays of orders with that status
// Example: { "pending": [order1, order3], "delivered": [order2] }
type GroupedOrders = Record<string, Order[]>;

// ─── Function ─────────────────────────────────────────────────────────────────

// Takes flat array of orders → returns object grouped by status field
//
// HOW IT WORKS (step-by-step with example):
//
//   Input: [{ id:'o1', status:'pending' }, { id:'o2', status:'delivered' }, { id:'o3', status:'pending' }]
//
//   Iteration 1: order = { id:'o1', status:'pending' }
//     → result = {} (empty, no 'pending' key yet)
//     → create: result['pending'] = []
//     → push:   result['pending'] = [{ id:'o1', status:'pending' }]
//
//   Iteration 2: order = { id:'o2', status:'delivered' }
//     → result = { pending: [...] } (no 'delivered' key yet)
//     → create: result['delivered'] = []
//     → push:   result['delivered'] = [{ id:'o2', status:'delivered' }]
//
//   Iteration 3: order = { id:'o3', status:'pending' }
//     → result = { pending: [o1], delivered: [o2] } ('pending' key EXISTS)
//     → skip create (array already there)
//     → push:   result['pending'] = [{ id:'o1',... }, { id:'o3',... }]
//
//   Final: { pending: [o1, o3], delivered: [o2] }
//
function groupOrdersByStatus(orders: Order[]): GroupedOrders {

    // Accumulator object — starts empty, builds up as we loop
    const result: GroupedOrders = {};

    // Loop through each order in the input array
    for (const order of orders) {

        // Extract the status string from this order
        // e.g. order = { id:'o1', status:'pending' } → status = 'pending'
        const status = order.status;
        console.log("logStatus: " + status)
        // Check: does result already have an array for this status?
        // First time seeing 'pending' → result['pending'] is undefined → create empty array
        // Second time seeing 'pending' → result['pending'] already exists → skip
        if (!result[status]) {
            console.log("logStatus: " + status)
            result[status] = [];
        }

        // Push this order into the correct status group
        // e.g. result['pending'].push({ id:'o1', status:'pending' })
        result[status].push(order);
    }

    // Return the grouped object
    // e.g. { pending: [{...}, {...}], delivered: [{...}] }
    return result;
}

// ─── Tests ────────────────────────────────────────────────────────────────────

describe('groupOrdersByStatus', () => {

    test('groups orders by status', () => {
        const input: Order[] = [
            { id: 'o1', status: 'pending' },
            { id: 'o2', status: 'delivered' },
            { id: 'o3', status: 'pending' },
        ];
        const result = groupOrdersByStatus(input);

        expect(result).toEqual({
            pending: [
                { id: 'o1', status: 'pending' },
                { id: 'o3', status: 'pending' },
            ],
            delivered: [
                { id: 'o2', status: 'delivered' },
            ],
        });
    });

    test('single status — all same', () => {
        const input: Order[] = [
            { id: 'o1', status: 'shipped' },
            { id: 'o2', status: 'shipped' },
        ];
        expect(groupOrdersByStatus(input)).toEqual({
            shipped: [
                { id: 'o1', status: 'shipped' },
                { id: 'o2', status: 'shipped' },
            ],
        });
    });

    test('each order has unique status', () => {
        const input: Order[] = [
            { id: 'o1', status: 'pending' },
            { id: 'o2', status: 'delivered' },
            { id: 'o3', status: 'cancelled' },
        ];
        const result = groupOrdersByStatus(input);

        // Each group has exactly 1 order
        expect(Object.keys(result)).toHaveLength(3);
        expect(result['pending']).toHaveLength(1);
        expect(result['delivered']).toHaveLength(1);
        expect(result['cancelled']).toHaveLength(1);
    });

    test('empty input returns empty object', () => {
        expect(groupOrdersByStatus([])).toEqual({});
    });

    test('single order returns single group', () => {
        const input: Order[] = [{ id: 'o1', status: 'pending' }];
        expect(groupOrdersByStatus(input)).toEqual({
            pending: [{ id: 'o1', status: 'pending' }],
        });
    });

    test('preserves order within groups', () => {
        const input: Order[] = [
            { id: 'o1', status: 'pending' },
            { id: 'o2', status: 'pending' },
            { id: 'o3', status: 'pending' },
        ];
        const result = groupOrdersByStatus(input);

        // Order should match insertion order: o1 → o2 → o3
        expect(result['pending'][0].id).toBe('o1');
        expect(result['pending'][1].id).toBe('o2');
        expect(result['pending'][2].id).toBe('o3');
    });
});
