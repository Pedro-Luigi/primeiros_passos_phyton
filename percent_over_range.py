entrada = [float(valor.strip()) for valor in input().split(',')]

# Define a função de normalização Min-Max.
def min_max_normalization(data):
    min_val = min(data)
    max_val = max(data)

    if max_val == min_val:
        return [0.0] * len(data)
    else:
        return [((x - min_val) * 100 / (max_val - min_val)) / 100 for x in data]

print(min_max_normalization(entrada))