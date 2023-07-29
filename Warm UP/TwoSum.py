# Two sum

lst = [2, 7, 11, 15]
target = int(input('Enter a number: '))


def two_sum(lst, target):
    for x in range(len(lst)):
        for y in range(x+1, len(lst)):
            if lst[x] + lst[y] == target:
                print(True)
 
            
two_sum(lst, target)
