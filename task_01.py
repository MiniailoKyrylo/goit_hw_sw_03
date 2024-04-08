import os
import shutil
import threading

# Переміщення файлу з джерела у призначення
def copy_files(source_file_path, target_file_path):
    
    """
        source_file_path (str): Директорія для копіювання файлів
        target_file_path (str): Дирикторія для збереження копій файлів
    """

    try:
        shutil.copy(source_file_path, target_file_path)
    except Exception as e:
        print(f"Помилка копіювання файлів {source_file_path}: {e}")

# Пошук усіх файлів та підкаталогів у вихідній директорії
def process_directory(source_dir, target_dir):
    
    """ 
        source_dir (str): Директорія для копіювання файлів
        target_dir (str): Дирикторія для збереження копій файлів
    """

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_file_path = os.path.join(root, file)
            
            # Отримання розширення файлу
            file_extension = os.path.splitext(file)[1][1:].lower()
            
            # Створення підкаталогу у призначенні за розширенням, якщо він ще не існує
            target_extension_dir = os.path.join(target_dir, file_extension)
            if not os.path.exists(target_extension_dir):
                os.makedirs(target_extension_dir)
            
            # Копіювання файлу у відповідний підкаталог за розширенням
            target_file_path = os.path.join(target_extension_dir, file)
            copy_files(source_file_path, target_file_path)

# Головний метод програми
def main(source_dir, target_dir):
    
    """ 
        source_dir (str): Директорія для копіювання файлів
        target_dir (str): Дирикторія для збереження копій файлів
    """

    # Перевірка та створення цільової директорії, якщо вона ще не існує
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Запуск обробки директорії та файлів в окремих потоках
    threads = []
    for root, _, _ in os.walk(source_dir):
        thread = threading.Thread(target=process_directory, args=(root, target_dir))
        threads.append(thread)
        thread.start()

    # Очікування завершення всіх потоків
    for thread in threads:
        thread.join()

if __name__ == "__main__":

    # Виклик головної функції з статичними директоріями
    main(r'folder', r'folder_copy_01')
