import random
import time

# Função de Quick Sort
def quick_sort(arr):
    comparisons = 0
    swaps = 0
    if len(arr) <= 1:
        return arr, comparisons, swaps
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    comparisons += len(arr) - 1 # todos os elementos são comparados ao menos uma vez
    swaps += len(left) + len(right) # a troca de elementos é necessária apenas na construção da sublista esquerda e direita

    # Aqui é feita a recursão
    left, comparisons_left, swaps_left = quick_sort(left)
    right, comparisons_right, swaps_right = quick_sort(right)

    # Ao combinar os sub-resultados, nenhuma troca ou comparação adicional é necessária
    comparisons += comparisons_left + comparisons_right
    swaps += swaps_left + swaps_right

    return left + middle + right, comparisons, swaps

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
        result, comparisons, swaps = quick_sort(data.copy())
        end_time = time.time()

        execution_time = end_time - start_time

        # Exibindo resultados
        print(f"Tamanho: {size}, Caso: {case.capitalize()}")
        print(f"Tempo de Execução: {execution_time:.6f} segundos")
        print(f"Quantidade de Trocas: {swaps}")
        print(f"Quantidade de Comparações: {comparisons}")
        print("-----")