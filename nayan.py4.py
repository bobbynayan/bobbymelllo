lst =(input("Enter string :"))
length = len(lst)
count = 0
for i in range(0, length):
    if lst[i] == 'a':
        count += 1
if count == 0:
    print("a is not found in given list")
else :
    print("a has frecuency as" , count, "in given list")
