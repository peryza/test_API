import requests
import json
# ссылка на API
url = 'https://reqres.in/api/users'
id_user = input()
# берем сразу из API данные с нужного айдишника
response = requests.get(url,params={'id':id_user})
data = json.loads(response.text)

user = data.get("data")
first_name = user.get("first_name")
last_name = user.get("last_name")
# вывод имени и фамилии на экран
print(first_name, last_name)
