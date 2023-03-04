# Обязательное ДЗ - доделать телефонный справочник с внешним хранилищем информации, 
# дополнить функционалом добавления информации, удаления и редактирования.


import json

db_path = 'phone_book.json'
welcome = 'Enter command: 1 - read & show | 2 - add record | 3 - search | 4 - init DB | q - Quit\n'
phone_book = {}

def print_book(book):
    for k,v in book.items():
        print (k," - ", end = " | ")
        for i,j in v.items():
           print (i, j, end = " | ")
        print()

def save_db(path, db):
    with open(path, 'w', encoding='utf-8') as fh:  # открываем файл на запись
        fh.write(json.dumps(db, ensure_ascii=False))  # преобразовываем словарь data в unicode-строку и записываем в файл
        print('БД успешно сохранена')

def load_db(path):
    # загрузить из json
    with open(path, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
        BD_local = json.load(fh)  # загружаем из файла данные в словарь data
    print('БД успешно загружена')
    return BD_local

def new_record(book):
    k=input("Put new name")
    a={}
    a['phone']=list(input('put phone').split())
    a['birthday']=input('put birthday')
    a['email']=input('put email')
    book[k]=a

try:
    phone_book=load_db(db_path)
except:
    phone_book = {
    'Иванов Иван Иванович':{'phone': ['+79235847585','+79132547524'] , 'email':"mail@gmail.ru"},
    'Петров Петр Петрович':{'phone': ['+79127121225','+71365475241']}}     
    print('База данных не найдена. Создана тестовая база')
action = None
while action != 'q':
    action = input(f'{welcome}').lower()
    if action == '1':
        print_book(phone_book)
    elif action == '2':
        new_record(phone_book)
    elif action == '3':
        print(action, ' -> ', db_path)
    elif action == '4':
        save_db(db_path, phone_book)
save_db(db_path, phone_book)