from os import system

system("cls")
size = int(input("No. of elements to be sorted ? "))
elem = [1]
elem[0] = int(input("Enter Element 1 : "))

for i in range(1, size):
    elem.append(int(input("Enter Element " + str(i + 1) + " : ")))

print("::Before Sorting::\n")
for i in range(0, size):
    print(":: " + str(elem[i]) + " ::\t")

revOrNot = input("Ascending(A) Or Descending(D) : ").upper()

if revOrNot is 'A':
    for i in range(0, size):
        for j in range(i, size):
            if elem[i] >= elem[j]:
                temp = elem[i]
                elem[i] = elem[j]
                elem[j] = temp
else:
    for i in range(0, size):
        for j in range(i, size):
            if elem[i] <= elem[j]:
                temp = elem[i]
                elem[i] = elem[j]
                elem[j] = temp

print("::After Sorting::\n")

for i in range(0, size):
    print(":: " + str(elem[i]) + " ::\t")