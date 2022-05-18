# sky.pro-game-broken_phone

## Инструкция

* У себя в консоли создаем папку и клонируем репозиторий
* создаем новую ветку
* запускаем main.py и оставляем сообщение (можно несколько)
* создаем новую ветку
* индексируем файлы
* пушим на сервер

если при пуше возникла ошибка, пробуем переименовать ветку и запушить еще раз

```bash
mkdir test
cd ./test
git clone https://github.com/golosovsa/sky.pro-game-broken_phone.git
cd ./sky.pro-game-broken_phone
python3 main.py 
git checkout -b <your_branche_name>
git add .
git commit -m "<your commit msg>"
git push origin <your_branche_name>
```

если произошла ошибка, то:
* переименовываем ветку
* пушим еще раз

```bash
git branch -m <new_branche_name>
git push origin <new_branche_name>
```

< ... > - символы больше и меньше для примера, их вводить не надо 