def three_numbers():
    
    numbers = []

    for x in range(10):
        for y in range(x, 10):
            for z in range(y , 10):
                numbers.append(f"{x}{y}{z}")

    result = ', '.join(numbers)

    print(result)

if __name__== '__main__':
    
    three_numbers()