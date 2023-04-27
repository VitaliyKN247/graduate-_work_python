import json
import datetime
from json import JSONEncoder

flag = 1
flag2 = 1


while (flag == 1):
    answer = int(input("Выберите действие:\n" 
          '1.Создание заметки\n' 
          '2.Вывод всех заметок\n'
          '3.Вывод определенной заметки\n'
          '4.Редактирование заметки:\n'
          '5.Удаление заметки\n'
          '6.Выход из программы\n'
          ))
    if answer == 1:
        if flag2 == True:
            data = {}
            data['note'] = []
            data['note'].append({
            'name': input('Введите заголовок: '), 
            'content': input('Введите содержимое: '),
            'date' : datetime.datetime.now()
            })
            class DateTimeEncoder(JSONEncoder):
                def default(self, obj):
                    if isinstance(obj, (datetime.date, datetime.datetime)):
                        return obj.isoformat()   
            with open('note.json', 'w') as outfile:
                employeeJSONData = json.dump(data, outfile,cls=DateTimeEncoder,ensure_ascii=False, indent=2)
                outfile.write('\n')
                flag2 = False
        else:
            new_data = {'name': input('Введите заголовок: '), 'content': input('Введите содержимое: ')} #создали переменную, включающую в себя данные, которые мы хотим добавить в уже имеющийся файл
            with open('note.json', encoding='utf8') as f: #Открываем файл
                data = json.load(f) #Получае все данные из файла (вообще все, да)
                data['note'].append(new_data) #Добавляем данные
            with open('note.json', 'w', encoding='utf8') as outfile: #Открываем файл для записи
                json.dump(data, outfile,ensure_ascii=False,cls=DateTimeEncoder, indent=2) #Добавляем данные (все, что было ДО добавления данных + добавленные данные)
        
    elif answer == 2:
        file = open('note.json')
        print(file.read())

    elif answer == 3:
        user_for_print = str(input('Введите название заметки, которую нужно открыть:  \n'))
        with open('note.json', 'r') as f:
            data = json.load(f)
            minimal = 0
        for txt in data['note']:
            if txt['name'] == user_for_print:
                print(txt)
            else:
                None
            minimal = minimal + 1

    elif answer == 4:
        user_for_edit= str(input('Введите название заметки, которую нужно редактировать:  \n'))
        with open('note.json', 'r') as f:
            data = json.load(f)
            minimal = 0
        for txt in data['note']:
            if txt['name'] == user_for_edit:
                data['note'].pop(minimal)
                new_data = {'name': input('Введите заголовок: '), 'content': input('Введите содержимое: ')}
                data['note'].append(new_data)
            else:
                None
            minimal = minimal + 1
        with open('note.json', 'w') as outfile:
            json.dump(data, outfile,ensure_ascii=False,cls=DateTimeEncoder)

    elif answer == 5:
        user_for_del = str(input('Введите название заметки, которое нужно удалить:  \n'))
        with open('note.json', 'r') as f:
            data = json.load(f)
            minimal = 0
        for txt in data['note']:
            if txt['name'] == user_for_del:
                data['note'].pop(minimal)
            else:
                None
            minimal = minimal + 1
        with open('note.json', 'w') as outfile:
            json.dump(data, outfile,ensure_ascii=False, indent=2)

    elif answer == 6:
        flag = False
            
    else:
        print("Неправильный ввод!\n",
              "-----------------")
       

