import os
from project.app.services import groupService, commonService
from project.tests.utils import randomUtil, authUtils
from project.app import main


DEFAULT_PUBLIC_UUID = "c95802ac-e465-11e8-9f32-f2801f1b9fd1"  # Joe.Customer@foo.com.invali
DEFAULT_ADMIN_UUID = "c957fece-e465-11e8-9f32-f2801f1b9fd1"  # sys.admin@foo.com.invali
DEFAULT_PUBLIC_CLIENT_ID = "CLTID-Zeq1LRso5q-iLU9RKCKnu"


def setup_dev_settings():
    # for using http instead of https
    os.environ['AUTHLIB_INSECURE_TRANSPORT'] = '1'

    # Application specific
    os.environ["APP_MODE"] = "dev"  # dev, test, or prod
    os.environ["APP_SECRET_KEY"] = "KlkdZyb5xrGpDcNkSBrDhe790ohLfuea"
    os.environ["APP_FLASK_SECRET_KEY"] = "wbr59q8tof3k2FfeSIvO"

    os.environ["APP_JWT_ISS"] = "https://localhost:9000"
    os.environ["APP_JWT_KEY"] = "BMcrqdcd7QeEmR8CXyU"

    # database config
    os.environ["APP_DB_CONNECTION_URI"] = "postgresql://postgres:P$F$xs+n?5+Ug3AU5PTe3q@localhost/postgres"
    os.environ["APP_DB_ENGINE_DEBUG"] = "False"


def create_public_group():

    group_name = "Group_" + randomUtil.random_string(6, 18)
    new_group = groupService.add_group(group_name)

    return new_group


def get_default_staff():

    bearer_token = _generate_jwt_token(DEFAULT_ADMIN_UUID)

    return {"user_uuid": DEFAULT_ADMIN_UUID, "token": bearer_token}


def _generate_jwt_token(user_uuid):

    authority_list = _get_authorities(user_uuid)
    oauth2_secret_key = main.global_config["APP_JWT_KEY"]
    token = authUtils.encode_auth_token(user_uuid, authority_list, oauth2_secret_key)

    return token.decode("utf-8")


def _get_authorities(user_uuid):
    if DEFAULT_PUBLIC_UUID == user_uuid:
        return ['CUST_ACCESS', 'CUST_PROFILE']
    elif DEFAULT_ADMIN_UUID == user_uuid:
        return ['STAFF_ACCESS', 'BATCH', 'SYSTEM']
    else:
        return None
