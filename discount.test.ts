// Shape of each item: must have price (per unit) and qty (quantity)
interface Item {
    price: number;
    qty: number;
}

// Takes array of items and a discount % (0–100), returns final total rounded to 2 decimals
function calcDiscountedTotal(items: Item[], discount: number): number {

    // Sum up subtotal: for each item multiply price × qty, then add all together
    const subtotal = items.reduce((sum, item) => sum + item.price * item.qty, 0);

    // Convert discount % to multiplier: 10% off → multiply by 0.9
    const multiplier = (100 - discount) / 100;

    // Apply discount to subtotal
    const total = subtotal * multiplier;

    // Round to 2 decimal places and return as number
    return parseFloat(total.toFixed(2));
}

// ─── Tests ────────────────────────────────────────────────────────────────────

describe('calcDiscountedTotal', () => {

    test('applies 10% discount correctly', () => {
        const items = [{ price: 120, qty: 2 }, { price: 50, qty: 1 }];
        // subtotal = 240 + 50 = 290 → 290 * 0.9 = 261.00
        expect(calcDiscountedTotal(items, 10)).toBe(261.00);
    });

    test('0% discount returns full subtotal', () => {
        const items = [{ price: 100, qty: 3 }];
        // subtotal = 300 → 300 * 1.0 = 300.00
        expect(calcDiscountedTotal(items, 0)).toBe(300.00);
    });

    test('100% discount returns 0', () => {
        const items = [{ price: 50, qty: 2 }];
        // subtotal = 100 → 100 * 0.0 = 0.00
        expect(calcDiscountedTotal(items, 100)).toBe(0.00);
    });

    test('rounds to 2 decimal places', () => {
        const items = [{ price: 10, qty: 1 }];
        // subtotal = 10 → 10 * (100-33)/100 = 10 * 0.67 = 6.70
        expect(calcDiscountedTotal(items, 33)).toBe(6.70);
    });

    test('empty items returns 0', () => {
        expect(calcDiscountedTotal([], 20)).toBe(0.00);
    });

    test('multiple items with qty > 1', () => {
        const items = [{ price: 200, qty: 3 }, { price: 100, qty: 2 }];
        // subtotal = 600 + 200 = 800 → 800 * 0.75 = 600.00
        expect(calcDiscountedTotal(items, 25)).toBe(600.00);
    });
});
