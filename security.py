
from user import User             # local package
from werkzeug.security import safe_str_cmp # safe string compare for password

# user list
users = {
    User(1, "claudio", "qwer")
}

# user mapping helpier
username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

# verify whether the username typed is on the username list
def authenticate(username, password):
    user = username_mapping.get(username, None) # .get() access the dictionary
    if user is not None and safe_str_cmp(user.password, password):
        return user

# verify whether the content of JWT Token (payload) has the user id
def identity(payload):
    userid = payload['identity']
    return userid_mapping.get(userid, None)