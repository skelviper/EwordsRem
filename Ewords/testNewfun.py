import sys
import msvcrt


def custom_input(prefix=""):
    """Custom string input that submits with space rather than enter"""
    concatenated_string = ""
    sys.stdout.write(prefix)
    sys.stdout.flush()
    while True:
        key = ord(msvcrt.getch())
        # If the key is enter or space
        if key == 32 or key == 13:
            break
        concatenated_string = concatenated_string + chr(key)
        # Print the characters as they're entered
        sys.stdout.write(chr(key))
        sys.stdout.flush()
    return concatenated_string


word = custom_input()
print(word)
