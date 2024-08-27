def separate_phase(lista):
    if isinstance(lista, str):
        return [x.strip() for x in lista.split(',')]
    return lista

final_list = list(set(separate_phase(input("Insira os dados separados por vírgula:"))))

print(sorted(final_list))
