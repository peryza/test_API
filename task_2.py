import json
import numpy

dept = []
unique_dept_list = []
new_data = {}


# ссчитываем исходные данные из файла
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# забираем отделы каждого работника
for worker in data:
    dept.append(worker['dept'])

# оставляем только уникальные и делаем из них массив
unique_dept = set(dept)
for i in unique_dept:
    unique_dept_list.append(i)

#обрабатываем данные для нового формата
k = 0
# цикл по уникальным отделам
for dept in unique_dept_list:
    avg_hours = 0
    count = 0
    people = []
    count_hour = 0
    dept_data = {}
    count_h_p = 0
    # цикл про сотрудникам
    for worker in data:
        people_data = {}
        # проверка на соответствие сотрудника отделу
        if dept == worker["dept"]:
            count += 1
            # проверка на то, есть ли у сотрудника выработанные часы
            if "hours" in worker:
                count_h_p += 1
                avg_hours += worker["hours"]
                people_data["hours"] = worker["hours"]
            # приображение данных к новому виду
            people_data["name"] = worker["name"]
            people_data["phone"] = worker["phone"]
            people.append(people_data)
            dept_data["count"] = count
            dept_data["people"] = people
    # округление
    dept_data["avg_hours"] = round(avg_hours/count_h_p)
    # запись данных в единое множество
    new_data[dept] = dept_data
# записываем данные в файл
with open('write_data.json', 'w', encoding='utf-8') as fw:
    json.dump(new_data,fw, sort_keys=True, indent=4, ensure_ascii=False)