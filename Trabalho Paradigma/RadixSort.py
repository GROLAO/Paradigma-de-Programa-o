import random
import time

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

    # Contagem de comparações e trocas
    num_comparisons = 0
    num_swaps = 0

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                num_comparisons += 1
                num_swaps += 1

    return arr, num_comparisons, num_swaps

def radix_sort(arr):
    max_element = max(arr)
    exp = 1
    comparisons = 0
    swaps = 0
    while max_element // exp > 0:
        arr, num_comparisons, num_swaps = counting_sort(arr, exp)
        comparisons += num_comparisons
        swaps += num_swaps
        exp *= 10

    return arr, comparisons, swaps

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
        
        # Medição de tempo
        start_time = time.time()
        sorted_data, comparisons, swaps = radix_sort(data.copy())
        end_time = time.time()

        execution_time = end_time - start_time

        # Exibindo resultados
        print(f"Tamanho: {size}, Caso: {case.capitalize()}")
        print(f"Tempo de Execução: {execution_time:.6f} segundos")
        print(f"Comparações: {comparisons}")
        print(f"Trocas: {swaps}")
        print("-----")