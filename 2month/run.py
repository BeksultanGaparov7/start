from main_lesson_7 import User, UserService

user = UserService()
user_service = User(name='Aslan', email='gaparovbeksultan7@gmail.com', age=18)
user.add_user(user_service)

find = user.get_user_by_email('gaparovbeksultan7@gmail.com')
if find:
    print(f' {find.name}, {find.email}, {find.age}')
