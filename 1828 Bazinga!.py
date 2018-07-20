n = int(input())
for c in range(n):
    x = c + 1
    sheldon, raj = input().split()
    if sheldon == raj:
        print('Caso #{}: De novo!'.format(x))
    elif sheldon == 'papel':
        if raj == 'tesoura' or raj == 'lagarto':
            print('Caso #{}: Raj trapaceou!'.format(x))
        elif raj == 'Spock' or raj == 'pedra':
            print('Caso #{}: Bazinga!'.format(x))
    elif sheldon == 'pedra':
        if raj == 'papel' or raj == 'Spock':
            print('Caso #{}: Raj trapaceou!'.format(x))
        elif raj == 'tesoura' or raj == 'lagarto':
            print('Caso #{}: Bazinga!'.format(x))
    elif sheldon == 'tesoura':
        if raj == 'Spock' or raj == 'pedra':
            print('Caso #{}: Raj trapaceou!'.format(x))
        elif raj == 'papel' or raj == 'lagarto':
            print('Caso #{}: Bazinga!'.format(x))
    elif sheldon == 'lagarto':
        if raj == 'pedra' or raj == 'tesoura':
            print('Caso #{}: Raj trapaceou!'.format(x))
        elif raj == 'Spock' or raj == 'papel':
            print('Caso #{}: Bazinga!'.format(x))
    elif sheldon == 'Spock':
        if raj == 'lagarto' or raj == 'papel':
            print('Caso #{}: Raj trapaceou!'.format(x))
        elif raj == 'tesoura' or raj == 'pedra':
            print('Caso #{}: Bazinga!'.format(x))
