## Установка зависимостей

Перед тем как запустить этот Django проект, нам необходимо установить 
зависимости, командой:

```bash
pip install -r requirements.txt
```

### Запуск миграцтя для БД

```bash
python manage.py makemigrations
python manage.py migrate
```
### Создание супер пользователя

Для для доступа и управления интерфейсом администратора необходимо
создать суперпользователя командой:

```bash
python manage.py createsuperuser
```

После всех вышеперечисленных манипуляция необходимо запустить наше приложение

```bash
python manage.py runserver
```

- Перейдите по ссылке чтобы открыть наше приложение: [http://127.0.0.1:8000/]
(http://127.0.0.1:8000/)

- Перейдите по ссылке чтобы открыть админ панель приложения: 
  [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- Перейдите по ссылке чтобы открыть документацию для API: 
  [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)
  
curl запрос для получения списка рейсов   
```bash 
curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/api/flights/
```

```bash
[
    {
        "id": 1,
        "flight_number": "SSJ100-9",
        "city_start": 1,
        "city_end": 2,
        "airplane": 1,
        "start_time": "10:43:48",
        "fact_time": "10:43:49",
        "status": "Вылетел"
    }
]
```