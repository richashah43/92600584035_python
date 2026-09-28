def numbers():
    for i in range(1, 6):
        yield i

for num in numbers():
    print(num)



#Another example with user input

def generate_numbers(n):
    for i in range(1, n + 1):
        yield i

n = int(input("Enter limit: "))

for num in generate_numbers(n):
    print(num)
