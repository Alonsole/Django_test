### Задание №3  
Работа с ORM  
Выгрузка каталога товаров из csv-файла с сохранением всех позиций в базе данных.  
Настройка.  
Перейти в main/settings и указать пароль подключения (Хост, порт) к postgresql. 
Потребуется создать ДатаБазу netology_import_phones!  
Проведены правки кода 25.09.2024г
DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.postgresql',  
        'NAME': 'netology_import_phones',  
        'HOST': '127.0.0.1',  
        'PORT': '5432',  
        'USER': 'postgres',  
        'PASSWORD': 'Ваш пароль',  
<img src="https://github.com/Alonsole/Django_test/blob/task3/res/catalog.png" width=45% />
