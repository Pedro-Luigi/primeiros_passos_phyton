numeros = list(map(float,
          input("Coloque a lista de números, separadas por vírgula:")
          .split(',')))

def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    tamanho_lista = len(lista_ordenada)
    ponto_medio = tamanho_lista // 2

    if tamanho_lista % 2 == 0 : return (lista_ordenada[ponto_medio - 1]+lista_ordenada[ponto_medio]) / 2
    else:return lista_ordenada[ponto_medio]

print("Mediana: ", calcular_mediana(numeros))