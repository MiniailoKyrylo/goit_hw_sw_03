import time

# Функція factorize визначає всі дільники числа number.
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

# Функція factorize_all визначає всі дільники для кожного числа у списку numbers.
def factorize_all(numbers):

    """
        numbers (list): Список цілих чисел, для яких потрібно знайти дільники.

        list: Список списків дільників для кожного числа у вихідному списку.
    """

    return [factorize(number) for number in numbers]

# Головний метод програми
def main(numbers):
    
    """ 
        numbers (list): Список чисел для обчислення
    """

    start_time = time.time()
    result = factorize_all(numbers)
    end_time = time.time()
    
    print("Час синхронного виконання:", end_time - start_time)
    print("Результат:", result) 

if __name__ == "__main__":

    # Виклик головної функції
    main([128, 255, 99999, 10651060])
    
    