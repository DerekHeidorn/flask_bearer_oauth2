import jwt
from project.app.services import commonService
from project.app import core

def decode_auth_token(auth_token):
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        # def decode(self,
        #            jwt,  # type: str
        #            key='',   # type: str
        #            verify=True,  # type: bool
        #            algorithms=None,  # type: List[str]
        #            options=None,  # type: Dict
        #            **kwargs):
        payload = jwt.decode(auth_token,
                             key=commonService.application_config_cache.get('oauth2_secret_key'),
                             algorithms=['HS512'])
        print("user:" + str(payload['sub']))
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'


def decode_auth_token_payload(jwt_token):
    """
    Decodes the auth token
    :param jwt_token:
    :return: payload as Dictionary
    """
    try:
        # def decode(self,
        #            jwt,  # type: str
        #            key='',   # type: str
        #            verify=True,  # type: bool
        #            algorithms=None,  # type: List[str]
        #            options=None,  # type: Dict
        #            **kwargs):
        payload = jwt.decode(jwt_token,
                             key=core.global_config["APP_JWT_KEY"],
                             algorithms=['HS512'])
        return payload
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
