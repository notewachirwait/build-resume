// Checks if all brackets in a string are balanced and correctly nested
// Handles: () [] {}
function isBracketsBalanced(code: string): boolean {

    // Stack to track opened brackets waiting to be closed
    const stack: string[] = [];

    // Map each closing bracket to its expected opening pair
    const matchingOpen: Record<string, string> = {
        ')': '(',
        ']': '[',
        '}': '{',
    };

    // Set of all opening brackets for quick lookup
    const openBrackets = new Set(['(', '[', '{']);

    // Walk through every character in the string
    for (const ch of code) {

        if (openBrackets.has(ch)) {
            // Opening bracket → push onto stack, wait for its closing pair
            stack.push(ch);

        } else if (ch in matchingOpen) {

            // We hit a closing bracket (e.g. ')' or ']' or '}')
            //
            // stack.pop() removes and returns the LAST opened bracket.
            // matchingOpen[ch] looks up what the correct opener should be.
            //
            // Example 1 — VALID: code = "([])"
            //   After seeing '(' and '[': stack = ['(', '[']
            //   ch = ']' → matchingOpen[']'] = '['
            //   stack.pop() returns '[' → '[' === '[' ✓ match! continue
            //
            // Example 2 — INVALID: code = "([)]"
            //   After seeing '(' and '[': stack = ['(', '[']
            //   ch = ')' → matchingOpen[')'] = '('
            //   stack.pop() returns '[' → '[' !== '(' ✗ mismatch! return false
            //
            // Example 3 — INVALID: code = ")"
            //   stack is empty
            //   stack.pop() returns undefined → undefined !== '(' ✗ return false
            //
            const popped = stack.pop();
            console.log("logMatching →", "ch:", ch, "| matchingOpen[ch]:", matchingOpen[ch], "| stack.pop():", popped);
            if (popped !== matchingOpen[ch]) {
                return false;
            }
        }
        // Any other character (letters, numbers, etc.) → ignore
    }

    // If stack is empty, all opened brackets were properly closed
    return stack.length === 0;
}

// ─── Tests ────────────────────────────────────────────────────────────────────

describe('isBracketsBalanced', () => {

    test('valid: expect with array matcher', () => {
        expect(isBracketsBalanced('expect(result).toBe([1,2,3])')).toBe(true);
    });

    test('invalid: missing opening paren', () => {
        expect(isBracketsBalanced('expect(result.toBe([1,2])')).toBe(false);
    });

    test('valid: nested object matchers', () => {
        expect(isBracketsBalanced('expect({a: 1}).toEqual({a:1})')).toBe(true);
    });

    test('valid: empty string', () => {
        expect(isBracketsBalanced('')).toBe(true);
    });

    test('invalid: wrong closing bracket type', () => {
        expect(isBracketsBalanced('([)]')).toBe(false);
    });

    test('invalid: unclosed bracket', () => {
        expect(isBracketsBalanced('foo(bar[')).toBe(false);
    });

    test('valid: no brackets at all', () => {
        expect(isBracketsBalanced('hello world')).toBe(true);
    });

    test('valid: deeply nested', () => {
        expect(isBracketsBalanced('fn([{a: (1+2)}])')).toBe(true);
    });

    test('invalid: extra closing bracket', () => {
        expect(isBracketsBalanced('fn()}')).toBe(false);
    });
});
