"""
The elves have found the encrypted code that protects the door to Santa’s workshop 🔐. The PIN has 4 digits, and it is hidden inside blocks like these:

[1++][2-][3+][<]
Write a function that deciphers the PIN from the code.

The code is made up of blocks between brackets [...] and each block generates one digit of the PIN.

A normal block has the form [nOP...], where n is a number (0-9) and after it there can be a list of (optional) operations.

The operations are applied in order to the number and are:

+ adds 1
- subtracts 1
The result is always a digit (mod 10 arithmetic), for example 9 + 1 → 0 and 0 - 1 → 9.

There is also the special block [<], which repeats the digit from the previous block.

If in the end there are fewer than 4 digits, you must return null.

🧩 Examples
decodeSantaPin('[1++][2-][3+][<]')
// "3144"

decodeSantaPin('[9+][0-][4][<]')
// "0944"

decodeSantaPin('[1+][2-]')
// null (only 2 digits)


"""


def decodeSantaPin(code: str) -> str:
    def block_decipher(block: str) -> str:
        number = int(block[0])
        optional = block[1:]
        for o in optional:
            if o == "+":
                number = number + 1 if number != 9 else 0
            elif o == "-":
                number = number - 1 if number != 0 else 9
        return str(number)

    block = ""
    final_code = ""

    for letter in code:
        if letter != "]":
            block += letter
        else:
            block = block[1:]
            if len(block) == 1 and block != "<":
                final_code += block
            elif block != "<":
                final_code += block_decipher(block)
            else:
                final_code += final_code[-1]
            block = ""

    if len(final_code) < 4:
        return None

    return final_code


print(decodeSantaPin("[9+][0-][4][<]"))
