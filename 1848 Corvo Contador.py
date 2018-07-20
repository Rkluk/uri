raven_eyes = {'*' : '1', '-' : '0'} #this dictionary will translate the eyes to numbers
caw_caw = 0 #counter to stop
num_lot = 0
num = ''
while caw_caw < 3:
    user = input()
    if user == 'caw caw':
        print(num_lot)
        caw_caw += 1
        num_lot = 0
    else:
        for c in user:
            num += raven_eyes[c]
        num_lot += int(num, 2)
        num = ''
