user = int(input())
for c in range(user):
    sentence = list(input())
    half = len(sentence) // 2
    a = sentence[:half]
    b = sentence[half:]
    a.reverse()
    b.reverse()
    c = ''.join(a) + ''.join(b)
    print(c)
