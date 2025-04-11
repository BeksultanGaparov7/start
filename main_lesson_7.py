from lesson_7 import Database



class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

class UserService:
    def __init__(self):
        self.db = Database()
    def add_user(self, user):
        if self.get_user_by_email(user.email):
            print('This email is already using')
            return
        self.db.add_user(user)
        print('User added')

    def get_user_by_email(self, email):
        user_data = self.db.get_user(email)
        if user_data:
            return User(name=user_data[1],email=user_data[2], age=user_data[3])
        else:
            print('ERROR: 404')

    def delete_user_by_email(self, email):
        delete = self.get_user_by_email(email)
        if delete:
            self.db.delete_user(email)
        else:
            print('ERROR: 404, NOT FOUND')


