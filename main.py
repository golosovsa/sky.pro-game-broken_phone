import getpass
import time


filename = f"{getpass.getuser()}_{time.time()}.txt"
user_input = input("Введи сообщение: ")
print(f"Сообщение: {user_input}\nИмя файла: '{filename}'")
if input("Сохранить? [y/n]: ") in ["Y", "y"]:
    with open(filename, "wt", encoding="utf-8") as fou:
        fou.write(user_input)
