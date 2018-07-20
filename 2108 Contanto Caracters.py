bigger = ''
while True:
    st = input()
    if st == '0':
        break
    st = st.split()
    numlist = []
    for c in st:
        if bigger == '' or len(c) >= len(bigger):
            bigger = c
        numlist.append(str(len(c)))
    r = '-'.join(numlist)
    print(r)
print('')
print('The biggest word: {}'.format(bigger))
