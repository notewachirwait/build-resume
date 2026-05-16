// Finds the first character that appears exactly once in the string (case-insensitive)
// Returns null if every character repeats
//
// HOW IT WORKS (step-by-step with example):
//
//   Input: 'sTrEEt'
//
//   Step 1 — Normalize to lowercase: 'street'
//
//   Step 2 — Count every character:
//     's' → 1
//     't' → 2   (appears at index 1 and 5)
//     'r' → 1
//     'e' → 2   (appears at index 3 and 4)
//
//   Step 3 — Walk the LOWERCASE string again, find FIRST char with count === 1:
//     index 0: 's' → count is 1 ✓ → return 's'
//
//   Another example: 'aabbcc'
//     counts: a→2, b→2, c→2
//     Walk string: 'a'→2, 'a'→2, 'b'→2, 'b'→2, 'c'→2, 'c'→2
//     No char has count 1 → return null
//
function firstUniqueChar(input: string): string | null {

    // Lowercase entire string so 'S' and 's' are treated as same character
    const lower = input.toLowerCase();

    // Map to count how many times each character appears
    // e.g. for 'street': { s:1, t:2, r:1, e:2 }
    const count = new Map<string, number>();

    // First pass: count occurrences of each character
    for (const ch of lower) {
        // If char exists → increment. If new → default 0 + 1 = 1
        count.set(ch, (count.get(ch) ?? 0) + 1);
    }

    // Second pass: walk string in order, return first char with count exactly 1
    // We iterate the lowercase string (not the Map) to preserve original order
    // Map iteration order would also work in JS, but this is more explicit
    for (const ch of lower) {
        if (count.get(ch) === 1) {
            // Found it! This is the first non-repeating character
            // e.g. 'street' → 's' has count 1 and appears first
            return ch;
        }
    }

    // Every character appears more than once → no unique char exists
    return null;
}

// ─── Tests ────────────────────────────────────────────────────────────────────

describe('firstUniqueChar', () => {

    test('returns first unique char', () => {
        // a:2, b:2, c:1, d:1, e:1 → first unique = 'c'
        expect(firstUniqueChar('aabbcde')).toBe('c');
    });

    test('returns null when all repeat', () => {
        // a:2, b:2, c:2 → no unique
        expect(firstUniqueChar('aabbcc')).toBeNull();
    });

    test('case-insensitive: sTrEEt → s', () => {
        // lowercase: 'street' → s:1, t:2, r:1, e:2 → first unique = 's'
        expect(firstUniqueChar('sTrEEt')).toBe('s');
    });

    test('empty string returns null', () => {
        expect(firstUniqueChar('')).toBeNull();
    });

    test('single character returns that character', () => {
        expect(firstUniqueChar('x')).toBe('x');
    });

    test('all same character returns null', () => {
        // 'aaaa' → a:4 → no unique
        expect(firstUniqueChar('aaaa')).toBeNull();
    });

    test('unique at end', () => {
        // a:2, b:2, c:1 → first unique = 'c' (at the end)
        expect(firstUniqueChar('aabbc')).toBe('c');
    });

    test('spaces count as characters', () => {
        // 'a a b' → a:2, ' ':2, b:1 → first unique = 'b'
        expect(firstUniqueChar('a a b')).toBe('b');
    });

    test('mixed case treated as same', () => {
        // 'AaBb' → lowercase 'aabb' → a:2, b:2 → null
        expect(firstUniqueChar('AaBb')).toBeNull();
    });
});
