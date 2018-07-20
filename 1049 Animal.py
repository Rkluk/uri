bone = str(input()).lower()
kind = str(input()).lower()
eat = str(input()).lower()
if bone == 'vertebrado':
    if kind == 'ave':
        if eat == 'carnivoro':
            animal = 'aguia'
        elif eat == 'onivoro':
            animal = 'pomba'
    elif kind == 'mamifero':
        if eat == 'onivoro':
            animal = 'homem'
        elif eat == 'herbivoro':
            animal = 'vaca'
elif bone == 'invertebrado':
    if kind == 'inseto':
        if eat == 'hematofago':
            animal = 'pulga'
        elif eat == 'herbivoro':
            animal = 'lagarta'
    elif kind == 'anelideo':
        if eat == 'hematofago':
            animal = 'sanguessuga'
        elif eat == 'onivoro':
            animal = 'minhoca'
print(animal)
