from abc import ABC, abstractmethod

class Notification(ABC):
    def __init__(self, message=""):
        self._message = message

    def set_message(self, message):
        self._message = message

    def get_message(self):
        return self._message

    @abstractmethod
    def send(self):
        pass


class SMSNotification(Notification):
    def send(self):
        print(f"📱 Отправка SMS: {self._message}")


class EmailNotification(Notification):
    def send(self):
        print(f"📧 Отправка Email: {self._message}")

notifications = [
    SMSNotification("Ваш код: 1234"),
    EmailNotification("Добро пожаловать в нашу рассылку!"),
    SMSNotification("У вас новое сообщение"),
    EmailNotification("Ваш аккаунт был обновлён.")
]

for note in notifications:
    note.send()