entrada = input()

lista = [int(x.strip()) if x.strip().isdigit() else None for x in entrada.split(',')]
contador_nulos = lista.count(None)

print(contador_nulos)