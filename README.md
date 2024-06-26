# SMS Генератор кода подтверждения 

Этот скрипт генерирует случайный код подтверждения и отправляет его пользователю в виде SMS-сообщения.

## Установка

1. Сохраните файлы `smsc_api.py` и `main.py` в одной директории.
2. Откройте терминал и перейдите в директорию с файлами.

## Настройка

Перед использованием скрипта, необходимо заменить значения `"login"` и `"password"` в файле `smsc_api.py` на ваши фактические учетные данные SMSC.RU.

## Использование

1. Запустите скрипт `main.py`:

```console
foo@compukter:~$ python3 main.py
```


2. Когда скрипт попросит, введите номер телефона получателя.
3. Скрипт сгенерирует случайный код подтверждения и отправит его в виде SMS-сообщения на указанный номер.
4. После отправки SMS-сообщения, скрипт выводит информационное сообщени, нажмите Enter для выхода из программы.

## Как это работает

1. Скрипт `main.py` импортирует необходимые функции из `smsc_api.py`.
2. Он запрашивает у пользователя номер телефона получателя.
3. Затем генерирует случайный код подтверждения из 6 цифр.
4. Скрипт использует класс `SMSC` из `smsc_api.py` для отправки SMS-сообщения с кодом подтверждения на указанный номер.
5. После отправки, скрипт выводит информационное сообщение и ждет, пока пользователь нажмет Enter для выхода.

##
