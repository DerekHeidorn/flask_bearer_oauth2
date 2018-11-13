from project.app.services import groupService, commonService
from project.tests.utils import randomUtil, authUtils


DEFAULT_PUBLIC_USER_PASSWORD = "fooBar@123"
DEFAULT_PUBLIC_UUID = "c95802ac-e465-11e8-9f32-f2801f1b9fd1"  # Joe.Customer@foo.com.invali
DEFAULT_ADMIN_UUID = "c957fece-e465-11e8-9f32-f2801f1b9fd1"  # sys.admin@foo.com.invali
DEFAULT_PUBLIC_CLIENT_ID = "CLTID-Zeq1LRso5q-iLU9RKCKnu"


def create_public_group():

    group_name = "Group_" + randomUtil.random_string(6, 18)
    new_group = groupService.add_group(group_name)

    return new_group


def get_default_staff():

    bearer_token = _generate_jwt_token(DEFAULT_ADMIN_UUID)

    return {"user_uuid": DEFAULT_ADMIN_UUID, "token": bearer_token}


def _generate_jwt_token(user_uuid):

    authority_list = _get_authorities(user_uuid)
    token = authUtils.encode_auth_token(user_uuid, authority_list, commonService.get_config_by_key("oauth2_secret_key"))

    return token.decode("utf-8")


def _get_authorities(user_uuid):
    if DEFAULT_PUBLIC_UUID == user_uuid:
        return ['CUST_ACCESS', 'CUST_PROFILE']
    elif DEFAULT_ADMIN_UUID == user_uuid:
        return ['STAFF_ACCESS', 'BATCH', 'SYSTEM']
    else:
        return None
