for c in range(int(input())):
    s = int(input());shots = [int(x) for x in input().split()];mov, hit = [input(), 0]
    for shot in range(s):
        if shots[shot] > 2 and mov[shot] == 'J' or shots[shot] <= 2 and mov[shot] == 'S':
            hit += 1
    print(hit)
