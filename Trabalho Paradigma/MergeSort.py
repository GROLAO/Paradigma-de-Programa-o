import random
import time

# Função de Merge Sort
def merge_sort(arr):
    comparisons = 0
    swaps = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Escrevendo chamadas recursivas
        comparisons, swaps = merge_sort(left_half)
        comparisons, swaps = merge_sort(right_half)

        # Lidando com comparações e swaps
        i = j = 0
        while i < len(left_half) and j < len(right_half):
            comparisons += 1
            if left_half[i] < right_half[j]:
                arr[i + j] = left_half[i]
                i += 1
            else:
                arr[i + j] = right_half[j]
                j += 1
                swaps += 1

        # Copiando os elementos restantes
        while i < len(left_half):
            arr[i + j] = left_half[i]
            i += 1
        while j < len(right_half):
            arr[i + j] = right_half[j]
            j += 1

    return comparisons, swaps

# Função para gerar dados para diferentes casos
def generate_data(size, case_type):
    if case_type == 'melhor':
        return list(range(1, size + 1))
    elif case_type == 'medio':
        return random.sample(range(1, size + 1), size)
    elif case_type == 'pior':
        return list(range(size, 0, -1))

# Testes para diferentes tamanhos e casos
sizes = [1000, 10000, 100000]
cases = ['melhor', 'medio', 'pior']

for size in sizes:
    for case in cases:
        data = generate_data(size, case)
        
        # Medição de tempo, trocas e comparações
        start_time = time.time()
        comparisons, swaps = merge_sort(data.copy())
        end_time = time.time()

        execution_time = end_time - start_time

        # Exibindo resultados
        print(f"Tamanho: {size}, Caso: {case.capitalize()}")
        print(f"Tempo de Execução: {execution_time:.6f} segundos")
        print(f"Quantidade de Trocas: {swaps}")
        print(f"Quantidade de Comparações: {comparisons}")
        print("-----")