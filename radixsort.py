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

def radixsort(arr):
    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

def benchmark(func, arr):
    start_time = time.time()
    func(arr)
    end_time = time.time()
    return end_time - start_time

sizes = [1000, 10000, 100000]
best_cases = []
average_cases = []
worst_cases = []

for size in sizes:
    arr = [i for i in range(size, 0, -1)]
    best_cases.append(benchmark(radixsort, arr))
    arr = [i % 1000 for i in range(size, 0, -1)]
    average_cases.append(benchmark(radixsort, arr))
    arr = [999 - i % 1000 for i in range(size, 0, -1)]
    worst_cases.append(benchmark(radixsort, arr))

print("Best Case:", best_cases)
print("Average Case:", average_cases)
print("Worst Case:", worst_cases)