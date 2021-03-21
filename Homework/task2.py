"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
"""
import timeit
import cProfile

def isPrime(n):
  for j in range(3, int(n**0.5)+1):
    if n%j==0:
      return 0
  return 1
def prime(n):
  primes = [2]
  i = 3
  while len(primes)<n:
    if isPrime(i) == 1:
      primes.append(i)
    i+=2
  return primes[n-1]


print(timeit.timeit('prime(10)', number=100, globals=globals()))           #0.0022569000000000027
print(timeit.timeit('prime(100)', number=100, globals=globals()))          #0.0530319
print(timeit.timeit('prime(1_000)', number=100, globals=globals()))        #1.1464983
print(timeit.timeit('prime(10_000)', number=100, globals=globals()))       #43.4622091

cProfile.run('prime(10_000)')
"""
114732 function calls in 0.476 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.476    0.476 <string>:1(<module>)
    52364    0.419    0.000    0.419    0.000 task2.py:16(isPrime)
        1    0.045    0.045    0.476    0.476 task2.py:21(prime)
        1    0.000    0.000    0.476    0.476 {built-in method builtins.exec}
    52365    0.010    0.000    0.010    0.000 {built-in method builtins.len}
     9999    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""


def sieve(number):
  n = 104729
  a = []
  for i in range(n + 1):
    a.append(i)
  a[1] = 0
  i = 2
  while i <= n:
    if a[i] != 0:
      j = i + i
      while j <= n:
        a[j] = 0
        j = j + i
    i += 1
  a = set(a)
  a.remove(0)
  a = list(a)
  a = sorted(a)
  return (a[number-1])

print(timeit.timeit('sieve(10)', number=100, globals=globals()))         #8.303962
print(timeit.timeit('sieve(100)', number=100, globals=globals()))        #8.2033867
print(timeit.timeit('sieve(1000)', number=100, globals=globals()))       #8.307769299999997
print(timeit.timeit('sieve(10000)', number=100, globals=globals()))      #8.2108818

cProfile.run('sieve(10_000)')
"""
         104736 function calls in 0.115 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.115    0.115 <string>:1(<module>)
        1    0.097    0.097    0.115    0.115 task2.py:54(sieve)
        1    0.000    0.000    0.115    0.115 {built-in method builtins.exec}
        1    0.001    0.001    0.001    0.001 {built-in method builtins.sorted}
   104730    0.016    0.000    0.016    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'remove' of 'set' objects}
"""


"""
В случае «Решета Эратосфена» большая часть времени ресурсов и времени тратиться на составления списка простых чисел,
чем на определение самого простого числа.
В случае короткого диапазона искомого простого числа, лучше воспользоваться алгоритмом без «Решета Эратосфена»
"""