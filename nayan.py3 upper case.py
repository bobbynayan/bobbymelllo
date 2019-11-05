upper=[ch for ch in string if ch.isupper() or ch.isspace()]
    if len(upper)==len(string):
        print('all upper')
    else:
        print("some character(s) not upper")

strings=['UPPERCAS!', 'UPPERCASe', 'UPPERCASE', 'MORE UPPERCASES']
for s in strings:
   up(s)
