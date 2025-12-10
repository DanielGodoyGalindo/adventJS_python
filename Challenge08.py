"""
Santa 🎅 wants to know what the first non-repeated letter is in a toy's name 🎁.

Write a function that takes a string and returns the first letter that is not repeated, ignoring uppercase and lowercase when counting,
but returning the letter as it appears in the string.

If there is none, return an empty string ("").

Examples:

findUniqueToy('Gift') // 'G'
// ℹ️ The G is the first letter that is not repeated
// and we return it exactly as it appears

findUniqueToy('sS') // ''
// ℹ️ The letters are repeated, since it doesn't distinguish uppercase

findUniqueToy('reindeeR') // 'i'
// ℹ️ The r is repeated (even if it's uppercase)
// and the e as well, so the first one is 'i'

// More cases:
findUniqueToy('AaBbCc') // ''
findUniqueToy('abcDEF') // 'a'
findUniqueToy('aAaAaAF') // 'F'
findUniqueToy('sTreSS') // 'T'
findUniqueToy('z') // 'z'
"""


def findUniqueToy(toy: str) -> str:
    toy = toy[::-1]
    toy_to_lower = toy.lower()[::-1]
    non_repeated_letter = ""
    for idx, letter in enumerate(toy_to_lower[::-1]):
        if toy_to_lower.count(letter) == 1:
            non_repeated_letter = toy[idx]
    return non_repeated_letter if non_repeated_letter else ""

print(findUniqueToy("z"))