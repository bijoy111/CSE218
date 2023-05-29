# print("Hello world")

# a = input("please give an input: ")

# print("Here is your output:", a)

with open("input.txt", "r") as inp:

    i = 0
    for line in inp:
        print("printing line:", i, line)
        i += 1
    inp.close()