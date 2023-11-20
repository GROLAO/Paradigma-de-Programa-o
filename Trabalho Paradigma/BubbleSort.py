import random
import time

# Função de Bubble Sort
def bubble_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
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
        comparisons, swaps = bubble_sort(data.copy())
        end_time = time.time()

        execution_time = end_time - start_time

        # Exibindo resultados
        print(f"Tamanho: {size}, Caso: {case.capitalize()}")
        print(f"Tempo de Execução: {execution_time:.6f} segundos")
        print(f"Quantidade de Trocas: {swaps}")
        print(f"Quantidade de Comparações: {comparisons}")
        print("-----")