
from project.app.models.user import User
from project.app.persist import userDao
from project.app.services.utils import userUtils


def buildMessage(key, message):
    return {key:message}    


def deleteUser(id):
    return userDao.deleteUser(id)


def updateUser(id, userToBeUpdated):
    return userDao.updateUser(id, userToBeUpdated)


def getUserById(id):
    return userDao.getUser(id)


def getUserByUsername(username):
    return userDao.getUserByUsername(username)


def addUser(username, password, firstName=None, lastName=None):

    userUtils.randomUserPrivateKey(32)

    newUser = User(firstName=firstName, lastName=lastName, username=username)
    newUser.statusCd = 'A'
    newUser.typeCd = '1'
    newUser.failedAttemptCnt = 0
    newUser.privateKey = userUtils.randomUserPrivateKey(32)
    newUser.passwordSalt = userUtils.randomUserPrivateKey(32) 
    newUser.passwordHash = userUtils.getHashedPassword(password, newUser.passwordSalt)
    userId = userDao.addUser(newUser)
    if userId:
        return userDao.getUser(userId)
    else:
        return None




 



