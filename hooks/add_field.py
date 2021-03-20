#!/usr/bin/python3
import json

try:
    with open('yabtm.conf.json') as json_file:
        data = json.load(json_file)
except IOError:
    print("В этой дирректории нет файла yabtm.conf.json")
name = input("введите имя поля: ")
ask = input("Введите вопрос для поля: ")
print("value: 1=текст 2=поле выбора")
value_type=int(input("1/2: "))
if(value_type == 1):
    value = "false"
elif(value_type == 2):
    value=[]
    value_numb=int(input("введите сколько будет вариантов выбора"))
    for i in range(value_numb):
        value.append(input(str(i+1)+") - "))
data["fields"][name]={"ask":ask,"value":value}
with open('yabtm.conf.json', 'w') as outfile:
    json.dump(data, outfile, ensure_ascii=False)



