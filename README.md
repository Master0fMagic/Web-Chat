Поднятия чата. Установить необходимые fw (список зависимостей находиться в файле requirements.txt). Создать базу данных, таблицы создать следующим образом: открыть среду выполнения python (python idle, запускается через терминал командой python), импортировать объект db из файла __init__.py (from web-chat import db), выполнить команду db.creat_all(). Создать файл config.py в корневой папке. Образец заполнения находится в файле config.txt После чего запустить файл с сервером app.py.  БД: PostgreSQL12

Технологии. Сервер чата написан на Flask, потому что это простой FW для создания серверов и я с ним сталкивался ранее. БД: PostgreSQL. до этого с ней не сталкивался, но много где о ней слышал, по этому решил попробовать именно ее. Для связи с базой использовал flask-sqlalchemy. Для авторизации использовался flask-login. 
