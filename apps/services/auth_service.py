from models.user import User

class AuthService:
    users = []
    current_user = None

    @classmethod
    def registration(cls, username, password, first_name, last_name):
        if not username or not username.strip():
            raise ValueError("bunday username bolishi mumkin emas")

        username = username.strip()
        print(username)

        for user in cls.users:
            if user.username == username:
                raise ValueError(f"{username} allaqachon mavjud")

        new_id = len(cls.users) + 1
        user = User(new_id, username, password, first_name, last_name)

        cls.users.append(user)
        return user

    @classmethod
    def login(cls, username, password):
        if not username or not username.strip():
            raise ValueError("bunday username bolishi mumkin emas")

        username = username.strip()

        for user in cls.users:
            if user.username == username and user.password == password:
                cls.current_user = user
                return user

        raise ValueError("username yoki parol xato, qayta urinib koring")
    
    @classmethod
    def logout(cls):
        if cls.current_user is None:
            raise ValueError("hozir login bulgan user yoq")
        
        cls.current_user = None
        return None