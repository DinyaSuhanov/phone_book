from os.path import exists
from csv import DictReader, DictWriter

file_name = 'phone.csv'                                 #имя создаваемого файла с данными
new_file_name = 'black_list.csv'                        #имя нового файла для копирования данных

class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt

class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt

def get_info():                                         #получение информации для записи в файл
    is_valid_first_name = False
    while not is_valid_first_name:                      #бесконечный цикл для проверки валидности
        try:
            first_name = input("Введите имя: ")
            if len(first_name) < 2:
                raise NameError("Это китайское имя? Имя не валидно!")
            else:
                is_valid_first_name = True
        except NameError as err:
            print(err)
            continue

    is_valid_last_name = False
    while not is_valid_last_name:
        try:
            last_name = input("Введите фамилию: ")
            if len(last_name) < 2:
                raise NameError("Это корейская фамилия? Фамилия не валидна!")
            else:
                is_valid_last_name = True
        except NameError as err:
            print(err)
            continue

    is_valid_phone = False
    while not is_valid_phone:
        try:
            phone_number = int(input("Введите номер: "))
            if len(str(phone_number)) != 11:
                raise LenNumberError("Городской номер??? Этот справочник только для сотовых. Неверная длина номера")
            else:
                is_valid_phone = True
        except ValueError:
            print("Не валидный номер!!!")
            continue
        except LenNumberError as err:
            print(err)
            continue

    return [first_name, last_name, phone_number]                #по итогу функция возвращает две строки и число


def create_file(file_name):                                     #создание файла для хранения вводимых данных
    # with - Менеджер контекста
    with open(file_name, "w", encoding='utf-8') as data:        #кодировку указывать необходимо, разные ос могут по разному воспринимать
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()


def read_file(file_name):                                       #чтение данных из файла
    with open(file_name, "r", encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)

def write_file(file_name, lst):
    res = read_file(file_name)
    for el in res:
        if el["Телефон"] == str(lst[2]):
            print("Такой телофон уже есть")
            return
    obj = {"Имя": lst[0], "Фамилия": lst[1], "Телефон": lst[2]}
    res.append(obj)
    with open(file_name, "w", encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)

def write_new_file(new_file_name, lst):
    res = read_file(new_file_name)
    res.append(lst)
    with open(new_file_name, "w", encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)

def copy(file_name = file_name, new_file_name = new_file_name):
    with open(file_name, 'r', encoding = 'utf-8') as data:
        f_reader = DictReader(data)
        lst_row = []
        for row in f_reader:
            lst_row.append(row)
        flag = False
        while not flag:
            try:
                number = int(input("Введите номер копируемой строки: "))
                if number > len(lst_row):
                    print("Проверьте корректность вводимого числа")
                else:
                    flag = True
            except ValueError:
                print("Введите цифру")
        if not exists(new_file_name):
            create_file(new_file_name)
        write_new_file(new_file_name, lst_row[number -1])

def main():
    while True:
        command = input("Введите команду: ")
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == 'r':
            if not exists(file_name):
                print("Файл отсутствует. Создайте его")
                continue
            print(*read_file(file_name))
        elif command == 'rr':
            if not exists(new_file_name):
                print("Файл отсутствует. Создайте его")
                continue
            print(*read_file(new_file_name))
        elif command == 'c':
            copy(file_name, new_file_name)

main()