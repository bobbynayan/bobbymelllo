l = ("Enter a string :")
length = len(l)
for i in range(length) :
    print("At indexes" , i,"and",(i-length), "element :",l[i])
    
print('length is: ',length)

for i in l[::-1]:
    print(i)
