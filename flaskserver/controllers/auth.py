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

    def get_user_by_login(self, username, hashed_password):
        """
        Login with username and password
        return user_dict
        """
        return UserModelManager().get_user(username=username, password=check_password_hash(hashed_password))

    def get_user(self, user_id):
        """
        Get a user by id
        return user_dict
        """
        return UserModelManager().get_user(id=user_id)