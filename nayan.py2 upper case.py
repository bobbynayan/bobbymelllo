famous_quote = input("Enter a one sentence quote: ").lower()
word = ""

for ltr in famous_quote:
    if ltr.isalpha() == True:
        word = word + ltr         
    else:
        if word > "g":
            print(word)
            word = ""
        else:
            word = ""
