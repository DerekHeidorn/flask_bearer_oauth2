
from authlib.flask.oauth2 import AuthorizationServer, ResourceProtector

from authlib.specs.rfc6749 import TokenMixin
from authlib.specs.rfc6750 import BearerTokenValidator
from project.app.web.utils import authUtils


class _OAuth2TokenMixin(TokenMixin):

    scope = None
    expires_in = None
    expires_at = None

    def get_scope(self):
        """A method to get scope of the authorization code. For instance,
        the column is called ``scope``::

            def get_scope(self):
                return self.scope

        :return: scope string
        """
        return self.scope

    def get_expires_in(self):
        """A method to get the ``expires_in`` value of the token. e.g.
        the column is called ``expires_in``::

            def get_expires_in(self):
                return self.expires_in

        :return: timestamp int
        """
        return self.expires_in

    def get_expires_at(self):
        """A method to get the value when this token will be expired. e.g.
        it would be::

            def get_expires_at(self):
                return self.created_at + self.expires_in

        :return: timestamp int
        """
        return self.expires_at


class _BearerTokenValidator(BearerTokenValidator):
    def authenticate_token(self, token_string):
        print("_BearerTokenValidator->authenticate_token called..." + token_string)
        # oAuth2Token = OAuth2Token()
        # return oAuth2Token
        payload = authUtils.decode_auth_token_payload(token_string)
        print("_BearerTokenValidator->payload:" + str(payload))

        token = _OAuth2TokenMixin()
        token.scope = payload['auth']
        token.expires_in = payload['exp'] - payload['iat']
        token.expires_at = payload['exp']

        return token

    def request_invalid(self, request):
        print("request_invalid->request:" + str(request))
        return False

    def token_revoked(self, token):
        print("token_revoked:" + str(token))
        return False


# ------------------------------------------------------------------------------
# Set up the Oauth Server
# ------------------------------------------------------------------------------
print("Creating AuthorizationServer...")
authorizationServer = AuthorizationServer()

# scopes definition
scopes = {
    'public': 'Public Access',
    'admin': 'Admin Access'
}

# protect resource
require_oauth = ResourceProtector()
require_oauth.register_token_validator(_BearerTokenValidator())


def init(app):

    print("initializing up AuthorizationServer...")
    authorizationServer.init_jwt_config(app)
    authorizationServer.init_app(app)
