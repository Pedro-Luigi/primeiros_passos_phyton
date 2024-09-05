idades = list(map(int, input().split(',')))

def agrupamento_idade(idades):
    grupos = {'0-18': 0, '19-35': 0, '36-50': 0, '51-70': 0, '71+': 0}
    for idade in idades:
        if idade <= 18:
            grupos['0-18'] += 1
        elif idade <= 35:
            grupos['19-35'] += 1
        elif idade <= 50:
            grupos['36-50'] += 1
        elif idade <= 70:
            grupos['51-70'] += 1
        else:
            grupos['71+'] += 1

    return grupos

print(agrupamento_idade(idades))