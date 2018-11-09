from project.app.models.user import User
from project.app.persist import baseDao, userDao, securityDao
from project.app.services.utils import userUtils


def is_user_valid(username, password):
    user = userDao.get_user_by_username(username)
    if user is not None:
        return userUtils.is_user_valid(user, password)
    else:
        return False


def delete_user(user_id):
    return userDao.delete_user(user_id)


def update_user(user_id, user_to_be_updated):
    return userDao.update_user(user_id, user_to_be_updated)


def get_users():
    return userDao.get_users()


def get_user_by_id(user_id):
    return userDao.get_user(user_id)


def get_user_by_username(username):
    return userDao.get_user_by_username(username)


def is_username_unique(username):
    return userDao.is_username_unique(username)


def get_user_by_username_and_validate(username, password):
    user = userDao.get_user_by_username(username)
    if user is not None:
        return {"user": user, "is_password_valid": userUtils.is_user_valid(user, password)}
    else:
        return {"user": None, "is_password_valid": False}


def add_public_user(client_id, username, password, first_name=None, last_name=None):

    userUtils.random_user_private_key(32)

    session = baseDao.get_session()
    security_group = securityDao.get_security_group_by_name(securityDao.SECURITY_GROUP_CUSTOMER_NAME,
                                                            session=session)

    new_user = User(first_name=first_name, last_name=last_name, username=username)
    new_user.status_cd = 'A'
    new_user.type_cd = '1'
    new_user.failed_attempt_count = 0
    new_user.private_key = userUtils.random_user_private_key(32)
    new_user.password_salt = userUtils.random_user_private_key(32)
    new_user.password_hash = userUtils.get_hashed_password(password, new_user.password_salt)

    new_user.security_groups.append(security_group)
    user_id = userDao.add_user(new_user, session=session)
    if user_id:
        return userDao.get_user(user_id)
    else:
        return None
