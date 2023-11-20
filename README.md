# Bubble Sort
# Improved Bubble Sort
# Insertion Sort
# Selection Sort
# Merge Sort
# Quick Sort



# Radix Sort

O Radix Sort é um algoritmo de ordenação que utiliza a técnica de contagem (counting) e ordenação (sorting) pelos dígitos. Ele é baseado em um princípio matemático simples: qualquer número, em qualquer base numérica, pode ser expresso como uma soma de múltiplos dessa base, cada um deles representado por um dígito.

Existem duas abordagens para implementa-lo: Least Significant Digit (LSD) e Most Significant Digit (MSD).

LSD: Processa os dígitos menos significativos primeiro e os dígitos mais significativos em último lugar. É simples e fácil de implementar, mas pode ser mais lento que o MSD, pois pode exigir a classificação de números que têm a mesma class do dígito atual várias vezes.

MSD: Processa os dígitos mais significativos primeiro e os dígitos menos significativos em último lugar. É mais rápido do que o LSD, pois os dígitos que estão sendo processados agora podem agrupar os números, o que pode levar a um tempo de execução mais rápido.

Embora o mesmo possa não ser a melhor opção em todos os casos, devido à sua dependência do tamanho do inteiro e ao número de dígitos, ele pode ser uma opção interessante em situações onde o tamanho dos dados é limitado
Esse algoritmo de ordenação utiliza a técnica de ordenação por chaves (bucket sort) e faz uso de uma representação binária. Ele ordena o array com base em cada dígito, do menos significativo para o mais significativo.

Para ilustrar, vamos supor que temos o seguinte array de números inteiros:

[170, 45, 75, 90, 802, 24, 2, 66] 
• Primeiro, o algoritmo determina o número de dígitos máximo que a maioria dos números possui. Neste caso, a maioria dos números possui dois dígitos, então o algoritmo se concentra nesses dígitos primeiro.
• Em seguida, o algoritmo cria um array de buckets vazios. Cada bucket representa um número entre 0 e 9.
• Em seguida, o algoritmo percorre cada elemento do array original e coloca o elemento no bucket correspondente à sua última casa decimal (dezena, neste caso). Por exemplo, o número 170 vai para o bucket 7.
• Depois de preencher todos os buckets, o algoritmo combina os elementos dos buckets de acordo com seus valores, para que os elementos menores sejam posicionados antes dos elementos maiores.
• O algoritmo repete esse processo para cada casa decimal, movendo para a casa decimal das centenas, e assim por diante, até que todos os dígitos do maior número no array sejam processados.

Após a execução do algoritmo, o array será ordenado em ordem crescente:
[2, 24, 45, 66, 75, 90, 170, 802]
Embora o Radix Sort seja eficiente para ordenar arrays grandes e em que a maioria dos números tenha um número pequeno de dígitos, ele pode ser lento se os números tiverem muitos dígitos e/ou se os dígitos de ordem mais significativa forem maiores. Além disso, o Radix Sort requer um espaço adicional de armazenamento proporcional ao tamanho do array.

## Tempos de Execução

O tempo de execução do radix sort, como outros algoritmos de classificação, é uma função da entrada. O tempo de execução depende do número de elementos a serem classificados (n) e do número de dígitos nos maiores números (d).
O tempo de execução do radix sort pode ser analisado em termos de melhor, pior e médio caso. No entanto, como o algoritmo utiliza o LSD (Least Significant Digit) ou o MSD (Most Significant Digit) para realizar a classificação, o tempo de execução não pode ser expresso diretamente em termos de notação Big O (por exemplo, O(n log n)).
Dito isso, podemos analisar o tempo de execução considerando as abordagens LSD e MSD.

•Para a abordagem LSD, o tempo de execução do radix sort é de O(nd) no pior caso, médio caso e melhor caso, já que ele processa todos os dígitos de todos os números em uma sequência.
•Para a abordagem MSD, o tempo de execução do radix sort é de O(n + nd) no pior caso, médio caso e melhor caso. Neste caso, o tempo de execução é influenciado não apenas pelo número de dígitos, mas também pelo número de partes na sequência.

Portanto, o tempo de execução pode variar dependendo da abordagem e do tamanho da entrada.
Em resumo, o tempo de execução depende do tamanho da entrada e da abordagem LSD ou MSD. O tempo de execução pode ser analisado em termos de melhor, pior e médio caso, e pode ser expresso em notação Big O, embora o LSD e o MSD não possam ser diretamente expressos em termos de O(n log n).</s

Dado que a análise de caso extremo é feita com base no pior caso possível, a abordagem LSD terá o melhor desempenho em relação ao caso médio e pior, já que seu tempo de execução é mais simples e direto, enquanto a abordagem MSD terá o melhor desempenho em relação ao caso médio e pior, já que utiliza uma partição da sequência para reduzir o tempo de execução.
No entanto, a análise do melhor caso em relação às abordagens LSD e MSD não é aplicável, já que o tempo de execução do radix sort não pode ser expresso diretamente em termos de O(n log n). Portanto, a abordagem LSD pode ser considerada como tendo um melhor desempenho em termos de tempo de execução do que a abordagem MSD.</s

### Exemplos de problemas para aplicação:

1.Problema de Ordenação de Candidatos em Eleições (USACO - United States of America Computing Olympiad). Neste problema, você deve classificar os candidatos em ordem decrescente com base no número de votos que receberam. Você pode aplicar o Radix Sort para classificar os candidatos com base no número de votos, pois ele pode lidar com números grandes e menores com eficiência.
2.Problema de Ordenação de Identificadores Únicos (Unique Identifiers). Neste problema, você deve classificar uma lista de identificadores únicos. O Radix Sort pode ser usado para classificar esses identificadores, pois pode lidar com números grandes e menores e classificá-los com base em dígitos específicos.
