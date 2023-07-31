
def first_unique_charatcter(string):

    indices_non_unique_char = {}
    indices_unique_chars = {}

    for x in range(len(string)):
        if string[x] in indices_non_unique_char:
            indices_non_unique_char[string[x]].append(x)
        else:
            # Check if the character is already in indices_unique_chars
            if string[x] in indices_unique_chars:
                # If it is, move it to indices_non_unique_char
                indices_non_unique_char[string[x]] = indices_unique_chars[string[x]]
                indices_non_unique_char[string[x]].append(x)
                # And remove it from indices_unique_chars
                del indices_unique_chars[string[x]]
            else:
                # If it's not in indices_unique_chars, create a new list for it
                indices_unique_chars[string[x]] = [x]

    return indices_unique_chars

print(first_unique_charatcter("loveleetcode"))