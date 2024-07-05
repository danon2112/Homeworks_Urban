name = 'Daniil'

def send_email(message, recipient, *, sender='university.help@gmail.com'):

    if not('@' in recipient) or not('@' in sender):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    domains = ['.com', '.net', '.ru']
    correct_domain = False
    for domain in domains:
        if recipient[len(recipient)-len(domain):] == domain:
            correct_domain = True
        if sender[len(sender)-len(domain):] == domain:
            correct_domain = True
            break
        else:
            correct_domain = False

    if not correct_domain:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
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

