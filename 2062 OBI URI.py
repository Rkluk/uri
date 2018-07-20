n = int(input())
palavras = input().split()
st = []
for c in palavras:
    if len(c) == 3:
        if c[:2] == 'UR':
            st.append('URI')
        elif c[:2] == 'OB':
            st.append('OBI')
        else:
            st.append(c)
    else:
        st.append(c)
st = ' '.join(st)
print(st)
