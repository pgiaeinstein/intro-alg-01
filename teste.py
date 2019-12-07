valores = [55, 92, 425, 86, 10, 64, 89, 177]

# Resolução do problema

def soma_valores_impar(lista_valores):
    soma = 0

    for item in valores:
        if item % 2 != 0:
            soma += item
            
    # prtin(soma)
    return soma

soma_valores_impar(valores)

# print(resultado)