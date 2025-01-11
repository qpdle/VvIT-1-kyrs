class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password

    def check_password(self, password):
        return self.__password == password

user = UserAccount('DaniilOrlov', 'DaniilOrlov@gmail.com', 'wasd')
user.set_password('123')
is_correct = user.check_password('123')
print(is_correct)
is_correct = user.check_password('wasd')
print(is_correct)