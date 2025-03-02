def generate_C(size):   
    inicio = ["C" * (5 * size)] * size 
    fim = inicio 
    meio = ["C" * size] * (3 * size)
    return "\n".join(inicio + meio + fim) 
size: int = 3

print(generate_C(size))
