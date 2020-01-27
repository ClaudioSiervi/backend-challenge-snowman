
from resources.user import User                       # local package
from werkzeug.security import safe_str_cmp # safe string compare for password


# verify whether the username typed is on the username list
def authenticate(username, password):
    user = User.find_by_username(username) 
    if user is not None and safe_str_cmp(user.password, password):
        return user

# verify whether the content of JWT Token (payload) has the user id
def identity(payload):
    user_id = payload['identity']
    return User.find_by_user_id(user_id)