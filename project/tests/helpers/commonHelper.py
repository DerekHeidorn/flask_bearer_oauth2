from project.app.services import userService
from project.tests.utils import randomUtil
from project.app.services.utils import userUtils
from project.app.web.utils import authUtils

DEFAULT_PUBLIC_USER_PASSWORD = "Foobar@123"
DEFAULT_PUBLIC_USERNAME = "Joe.Customer@foo.com.invali"
DEFAULT_ADMIN_USERNAME = "sys.admin@foo.com.invali"


def createPublicUser():

    username = randomUtil.randomUsername()
    password = DEFAULT_PUBLIC_USER_PASSWORD
    first_name = "FirstNm_" + randomUtil.randomString(6, 10)
    last_name = "LastNm_" + randomUtil.randomString(6, 10)

    newUser = userService.addUser(username, password, first_name, last_name)

    return newUser

def getDefaultStaff():

    staff = userService.getUserByUsername(DEFAULT_ADMIN_USERNAME)
    assert staff is not None
    bearerToken = _generateJwtToken(staff)

    return {"user": staff, "token": bearerToken}

def _generateJwtToken(user):
    # print("client:" + str(client))
    # print("grant_type:" + str(grant_type))
    # print("user:" + str(user))
    # print("scope:" + str(scope))

    authorities = userUtils.getUserAuthorities(user)
    #print("authorities:" + str(authorities))
    token = authUtils.encodeAuthToken(user, authorities)
    #print("token:" + str(token ))

    return token.decode("utf-8")