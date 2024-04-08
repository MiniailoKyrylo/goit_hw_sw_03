import time
import multiprocessing

# Визначає всі дільники числа number.
def factorize(number):
    """
        number (int): Ціле число, для якого потрібно знайти дільники.

        list: Список усіх дільників числа number.
    """

    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

# Обчислює всі дільники для кожного числа у списку паралельно, використовуючи кілька ядер процесора.
def factorize_all_parallel(numbers):
    """
        numbers (list): Список цілих чисел, для яких потрібно знайти дільники.

        list: Список списків дільників для кожного числа у вихідному списку.
    """

    # Створення пула процесів з використанням кількох ядер процесора
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    
    # Використання функції map для розпаралелювання обчислень
    result = pool.map(factorize, numbers)
    
    # Завершення роботи пула процесів
    pool.close()
    
    # Очікування завершення всіх процесів у пулі
    pool.join()
    return result

# Головний метод програми
def main(numbers):
    
    """ 
        numbers (list): Список чисел для обчислення
    """

    start_time = time.time()
    result = factorize_all_parallel(numbers)
    end_time = time.time()
    
    print("Час паралельного виконання:", end_time - start_time)
    print("Результат:", result)

if __name__ == "__main__":

    # Виклик головної функції
    main([128, 255, 99999, 10651060])
    
    
