# numbers = []
# i = 0

def print_list(max_number):
    numbers = []
    i = 0

    while i < max_number:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")
    for num in numbers:
        print(num)

def print_list_too(max_number):
    numbers = []
    i = 0

    for i in range(0, max_number):
        print(f"At the top i is {i}")
        numbers.append(i)

    print("The numbers: ")
    for num in numbers:
        print(num)

print_list_too(int(input("> ")))
