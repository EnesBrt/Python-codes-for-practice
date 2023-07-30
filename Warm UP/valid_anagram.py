def find_anagram(s, t):
    char_count_s = {}
    char_count_t = {}

    for x in range(len(s)):

        if s[x] in char_count_s:
            char_count_s[s[x]] += 1
        else:
            char_count_s[s[x]] = 1
    

    for y in range(len(t)):

        if t[y] in char_count_t:
            char_count_t[t[y]] += 1
        else:
            char_count_t[t[y]] = 1
    

    if char_count_s == char_count_t:
        return True
    else:
        return False

print(find_anagram("car","rac"))