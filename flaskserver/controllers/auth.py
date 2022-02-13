from werkzeug.security import check_password_hash, generate_password_hash
from flaskserver.models.users import UserModelManager

class UserAPI:

    def register_user(self, username, email, unhashed_password):
        """
        Register a user.
        return user_dict
        """
        return UserModelManager().create_user(
                username=username,
                email=email,
                password=generate_password_hash(unhashed_password)
            )

    def get_user_by_login(self, username, unhashed_password):
        """
        Login with username and password
        return user_dict
        """
        user = UserModelManager().get_user(username=username)
        if not user:
            return None
        password = user.password
        if check_password_hash(password, unhashed_password):
            return user
        return None

    def get_user(self, user_id):
        """
        Get a user by id
        return user_dict
        """
        return UserModelManager().get_user(id=user_id)