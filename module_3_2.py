name = 'Daniil'

def send_email(message, recipient, *, sender='university.help@gmail.com'):

    if not '@' in recipient or recipient == '@':
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    if not '@' in sender or sender == '@':
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    if not recipient.endswith('.com') and not recipient.endswith('.ru') and not recipient.endswith('.net'):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    if not sender.endswith('.com') and not sender.endswith('.ru') and not sender.endswith('.net'):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return




    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
        return
    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    return

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Пожалуйста, исправьте задание', 'urban.studentmail.ru', sender='urban.teachermail.ru')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
send_email('Вы видите это сообщение как лучший студент курса!', '@', sender='urban.info@gmail.com')
