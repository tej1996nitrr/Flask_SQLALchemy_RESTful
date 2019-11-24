from werkzeug.security import safe_str_cmp
#in memory table of registered users

from Models.user import UserModel
#
# userid_mapping={
# 1:
# {
# 'id':1,
# 'username':'harry',
# 'password':'potter'}
# }

# users = [
#     User(1, 'user1', 'abcxyz'),
#     User(2, 'user2', 'abcxyz'),
# ]

# username_table = {u.username: u for u in users}
# userid_table = {u.id: u for u in users}

def authenticate(username, password):
    # user = username_table.get(username, None)
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    
    return UserModel.find_by_id(user_id)
    # return userid_table.get(user_id, None)