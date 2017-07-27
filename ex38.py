ten_things = "Apples,Oranges,Crows,Telephone,Light,Sugar"
print("Ten_things: ", ten_things)
print(f"Ten_things: {ten_things}")

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(',')
print("Stuff: ", stuff)
print(f"Stuff: {stuff}")

more_stuff = ["Day", "Night", "Song", "Frisbee",
            "Corn", "Banana", "Girl", "Boy"]
print("more_stuff: ", more_stuff)

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Le's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop()) # pop from backward

stuff1 = ' '.join(stuff)
print("stuff1: ", stuff1)
print(' '.join(stuff))
print('#'.join(stuff[3:5])) # super stellar!
