def find_anagram(s, t):
    for x in s:
        for y in t:
            if y in s:
                return True
            else:
                return False


print(find_anagram("car","rat"))