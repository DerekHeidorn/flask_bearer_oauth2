import os
from app.services import groupService
from tests.utils import randomUtil, authUtils
from app import core


DEFAULT_PUBLIC_UUID = "c95802ac-e465-11e8-9f32-f2801f1b9fd1"  # Joe.Customer@foo.com.invali
DEFAULT_PUBLIC_SUBSCRIBED_UUID = "14468f27-44e8-4fc3-8cc6-3a48c80fd5aa"  # Joe.Subscribed@foo.com.invali
DEFAULT_PUBLIC_GROUP_SUBSCRIBED_UUID = "d71b920a-04a9-44d3-beda-a736601a64c5"  # Joe.Group.Subscribed@foo.com.invali
DEFAULT_ADMIN_UUID = "c957fece-e465-11e8-9f32-f2801f1b9fd1"  # sys.admin@foo.com.invali
DEFAULT_PUBLIC_CLIENT_ID = "CLTID-Zeq1LRso5q-iLU9RKCKnu"

GROUP_THE_AVENGERS_GROUP_ID = 1
GROUP_BROWN_COATS_GROUP_ID = 2
GROUP_FITNESS_PAL_GROUP_ID = 3
GROUP_ZOMBIE_APOCALPSE_GROUP_ID = 4
GROUP_COMPANY_ABC_WORKOUT_GROUP_ID = 5


def setup_dev_settings():
    # for using http instead of https
    os.environ['AUTHLIB_INSECURE_TRANSPORT'] = '1'

    # Application specific
    os.environ["APP_MODE"] = "dev"  # dev, test, or prod
    os.environ["APP_SECRET_KEY"] = "KlkdZyb5xrGpDcNkSBrDhe790ohLfuea"
    os.environ["APP_SHARED_SECRET_KEY"] = "MD7VBOYXMQxa2BvtLwu9PtBTuqbKGlJ9TIcB0n9M"
    os.environ["APP_FLASK_SECRET_KEY"] = "wbr59q8tof3k2FfeSIvO"

    os.environ["APP_JWT_ISS"] = "https://localhost:9000"
    os.environ["APP_JWT_KEY"] = "BMcrqdcd7QeEmR8CXyU"

    # database config
    os.environ["APP_DB_CONNECTION_URI"] = "postgresql://postgres:P$F$xs+n?5+Ug3AU5PTe3q@localhost/groups"
    os.environ["APP_DB_ENGINE_DEBUG"] = "False"

    os.environ["APP_EXTERNAL_API_USERS"] = ""


def create_public_group():

    group_name = "Group_" + randomUtil.random_string(6, 18)
    group_de = 'Some random description'
    new_group = groupService.add_group(group_name, group_de)

    return new_group


def get_group(group_id):
    return groupService.get_group_by_id(group_id)


def get_default_staff():

    bearer_token = _generate_jwt_token(DEFAULT_ADMIN_UUID)

    return {"user_uuid": DEFAULT_ADMIN_UUID, "token": bearer_token}


def get_default_public_user():

    bearer_token = _generate_jwt_token(DEFAULT_PUBLIC_UUID)

    return {"user_uuid": DEFAULT_PUBLIC_UUID, "token": bearer_token}


def _generate_jwt_token(user_uuid):

    authority_list = _get_authorities(user_uuid)
    print("authority_list=" + str(authority_list))
    oauth2_secret_key = core.global_config["APP_JWT_KEY"]
    token = authUtils.encode_auth_token(user_uuid, authority_list, oauth2_secret_key)

    return token.decode("utf-8")


def _get_authorities(user_uuid):
    if DEFAULT_PUBLIC_UUID == user_uuid:
        return ['CUST_ACCESS', 'GRP_ACCESS', 'RPT_ACCESS']
    elif DEFAULT_ADMIN_UUID == user_uuid:
        return ['ADM_ACCESS', 'GRP_ACCESS', 'GRP_ADMIN', 'RPT_ACCESS', 'BATCH_ACCESS', 'SYSTEM_ACCESS']
    else:
        return None
