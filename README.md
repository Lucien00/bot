CatBot
======

CatBot - Telegram-бот, присылающий фото котиков.

Установка
---------

Создайте виртуальное окружение и активируйте его. Потом в виртуальном окружении выполните:

..code-block:: text

    pip install -r requirements.txt

Положите картинки котиков в папку images. Название файлов должно начинаться с cat, а заканчиваться.jpg, например cat858549.jpg

Настройка
---------

Cоздайте файл settings.py и добавьте туда следующие настройки:

.. code-block:: python

    PROXY = {'proxy_url': 'socks5://ВАШ_SOCKS5_ПРОКСИ:1080',
        'urllib3_proxy_kwargs': {'username': 'ЛОГИН', 'password': 'ПАРОЛЬ'}}

    API_KEY = "API-ключ, который Вы получили у BotFather"

    USER_EMOJI = [':smiley_cat:', ':smiling_imp:', ':panda_face:', ':dog:']

Запуск
------

В активированном виртуальном окружении выполните:

.. code-block:: text

    python3 bot.py
