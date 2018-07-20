from fractions import gcd
fuel, primes = [int(input()), []]
while len(primes) < 10:
    prim = True
    if fuel % 2 == 0:
        prim = False
        pass
    else:
        for check in range(3, fuel // 2, 2):
            if gcd(check, fuel) != 1:
                prim = False
                break
    if prim:
        primes.append(fuel)
    fuel += 1
kmh = sum(primes);h = 60000000 // kmh;d = h // 24
print('{} km/h\n{} h / {} d'.format(kmh, h, d))
