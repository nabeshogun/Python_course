def checker(a):
    a = a.split('.')
    check_list = ["ru", "com", "net"]
    counter = 0
    for i in range(len(check_list)):
        if a[len(a) - 1] != check_list[i]:
            counter += 1
            if counter > 2:
                return False
        else:
            return True


def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if recipient.find('@') == -1 or sender.find('@') == -1:
        print("Невозможно отправить письмо с адреса", sender, "на адрес ", recipient)
    elif checker(recipient) == 0 or checker(sender) == 0:
        print("Невозможно отправить письмо с адреса", sender, "на адрес ", recipient)
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
