s, t, f = map(int, input().split())
h = s + t if s + t < 23 else s + t - 24
h = h + f if 24 > h + f >= 0 else 24 + (h + f)
print(h)
