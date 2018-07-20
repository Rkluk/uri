n = int(input())
for c in range(n):
    sheldon, raj = input().split()
    if sheldon == raj:
        print('empate')
    elif sheldon == 'papel':
        if raj == 'tesoura' or raj == 'lagarto':
            print('sheldon')
        elif raj == 'spock' or raj == 'pedra':
            print('rajesh')
    elif sheldon == 'pedra':
        if raj == 'papel' or raj == 'spock':
            print('sheldon')
        elif raj == 'tesoura' or raj == 'lagarto':
            print('rajesh')
    elif sheldon == 'tesoura':
        if raj == 'spock' or raj == 'pedra':
            print('sheldon')
        elif raj == 'papel' or raj == 'lagarto':
            print('rajesh')
    elif sheldon == 'lagarto':
        if raj == 'pedra' or raj == 'tesoura':
            print('sheldon')
        elif raj == 'spock' or raj == 'papel':
            print('rajesh')
    elif sheldon == 'spock':
        if raj == 'lagarto' or raj == 'papel':
            print('sheldon')
        elif raj == 'tesoura' or raj == 'pedra':
            print('rajesh')
