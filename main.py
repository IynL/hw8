import logging

logging.basicConfig(filename='error_log.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def divide_numbers():
    logging.debug('5Программа начала работу.')
    
    try:
        num1 = float(input("первое число: "))
        num2 = float(input("второе число: "))
        
        logging.debug(f'Пользователь ввел числа: {num1}, {num2}')
        
        result = num1 / num2
        
        logging.info(f'все норм. Результат: {result}')
        print(f'Результат: {result}')
    
    except ZeroDivisionError:
        logging.error('Деление на 0.')
        print("Нельзя делить на ноль!")
    
    except ValueError:
        logging.error('не те числа.')
        print("Некорректный ввод.")
    
    except Exception as e:
        logging.error(f'Неизвестная ошибка: {e}')
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    divide_numbers()
