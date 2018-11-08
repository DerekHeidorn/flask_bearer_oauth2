from project.app.services import userService
from project.tests.utils import randomUtil
from project.app.services.utils import userUtils
from project.app.web.utils import authUtils

DEFAULT_PUBLIC_USER_PASSWORD = "fooBar@123"
DEFAULT_PUBLIC_USERNAME = "Joe.Customer@foo.com.invali"
DEFAULT_ADMIN_USERNAME = "sys.admin@foo.com.invali"
DEFAULT_PUBLIC_CLIENT_ID = "CLTID-Zeq1LRso5q-iLU9RKCKnu"


def create_public_user():

    username = randomUtil.random_username()
    password = DEFAULT_PUBLIC_USER_PASSWORD
    first_name = "FirstNm_" + randomUtil.random_string(6, 10)
    last_name = "LastNm_" + randomUtil.random_string(6, 10)

    new_user = userService.add_public_user(DEFAULT_PUBLIC_CLIENT_ID, username, password, first_name, last_name)

    return new_user


def get_default_staff():

    staff = userService.get_user_by_username(DEFAULT_ADMIN_USERNAME)
    assert staff is not None
    bearer_token = _generate_jwt_token(staff)

    return {"user": staff, "token": bearer_token}


def _generate_jwt_token(user):
    # print("client:" + str(client))
    # print("grant_type:" + str(grant_type))
    # print("user:" + str(user))
    # print("scope:" + str(scope))

    authorities = userUtils.get_user_authorities(user)
    # print("authorities:" + str(authorities))
    token = authUtils.encode_auth_token(user, authorities)
    # print("token:" + str(token ))

    return token.decode("utf-8")
