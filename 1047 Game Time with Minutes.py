ihour, iminute, fhour, fminute = input().split()
ihour = int(ihour)
iminute = int(iminute)
fhour = int(fhour)
fminute = int(fminute)
if ihour < fhour and iminute < fminute:
    hours = fhour - ihour
    minutes = fminute - iminute
elif ihour == fhour and iminute < fminute:
    hours = 0
    minutes = fminute - iminute
elif ihour == fhour and iminute > fminute:
    hours = 0
    minutes = 60 - (iminute - fminute)
elif ihour == fhour and iminute == fminute:
    hours = 24
    minutes = 0
elif ihour > fhour and iminute == fminute:
    hours = 24 - (ihour - fhour)
    minutes = 0
elif ihour < fhour and iminute > fminute:
    hours = fhour - ihour - 1
    minutes = 60 - (iminute - fminute)
elif ihour < fhour and iminute == fminute:
    hours = fhour - ihour
    minutes = 0
elif ihour > fhour and iminute < fminute:
    hours = 24 - (ihour - fhour)
    minutes = fminute - iminute
elif ihour > fhour and iminute > fminute:
    hours = 24 - (ihour - fhour) - 1 
    minutes = 60 - (iminute - fminute)
print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hours, minutes))
