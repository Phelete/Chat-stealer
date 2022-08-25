import requests
token=input("Введите токен от бота: ")
owner_chat_id=input("Введите чат айди владельца: ")
your_chat_id=input("Введите ваш чат айди: ")
api_url=f"https://api.telegram.org/bot{token}"
bot_name=requests.get(f"{api_url}/getme").json()["result"]["username"]
owner_name=requests.get(f"{api_url}/getChat?chat_id={owner_chat_id}").json()["result"]["username"]
print(f"Имя бота: @{bot_name}")
print(f"Имя владельца бота: @{owner_name}")
while 1:
    input("Теперь напишите что либо боту чтобы было кому писать, после нажмите Enter.")
    try:
        msg_count=requests.get(f"{api_url}/sendMessage?text=Checking message_id&chat_id={your_chat_id}").json()["result"]["message_id"]-1
        break
    except:
        print("Бот не смог отправить вам сообщение скорее всего вы не написали ему.")
        continue
print(f"Колличество сообщений: {msg_count}")
start_msg=int(input("С какого сообщения пересылать: "))
for i in range(start_msg, msg_count):
    try:
        req=requests.get(f"{api_url}/forwardMessage?chat_id={your_chat_id}&from_chat_id={owner_chat_id}&message_id={i}")
        if req.status_code == 200:
            print(f"Сообщение {i+1} пересланно успешно.")
        else:
            print(f"Сообщение {i+1} не удалось переслать.")
    except KeyboardInterrupt:
        print("Остановка.")
        break
    except:
        print(f"Сообщение {i} не удалось переслать.")
        continue