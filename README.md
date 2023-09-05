### Описание проекта:

Тестовое задание ,  создал API на основе Django Rest Framework каталог исполнителей и их альбомов с песнями такой структуры

- Исполнитель
    - Имя исполнителя
- Альбом
    - Исполнитель
    - Год выпуска
    - Песня
        - название песни
- Песня
    -  Название
    -  Порядковый номер в альбоме

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:


```
cd tests
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры запросов к API:

Получить список всех альбомов (GET):
```
http://127.0.0.1:8000/api/v1/album/

 {
        "id": 1,
        "name": "Имя альбома",
        "year": год,
        "songer": "Имя исполнителя ",
        "songs": [
            {
                "name_music": "Название песни"
            },
        ]
    },
```

Получить определеную песню  (GET):
```
http://127.0.0.1:8000/api/v1/songs/

 {
        "id": 1,
        "name_music": "Название песни",
        "number": Порядковый номер в альбоме,
        "album": "Название альбома"
    }
```

Получить определеного исполнителя (GET):
```
http://127.0.0.1:8000/api/v1/songer/
{
        "id": 1,
        "name": "никнейм исполнителя"
    }
```
Документация к API
```
http://127.0.0.1:8000/swagger/
```