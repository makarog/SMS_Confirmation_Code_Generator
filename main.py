import random
import string
from smsc_api import *

# Запрашиваем номер телефона у пользователя
phone_number = input("Введите номер телефона получателя: ")

# Генерируем случайный код подтверждения
confirmation_code = ''.join(random.choices(string.digits, k=6))

# Отправляем SMS с кодом подтверждения
sms = SMSC()
sms.send_sms(phone_number, f"Ваш код подтверждения: {confirmation_code}")

print(f"SMS-сообщение с кодом подтверждения '{confirmation_code}' отправлено на номер {phone_number}")

print("Нажмите Enter для выхода...")
input()
