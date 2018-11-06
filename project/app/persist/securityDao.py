
from project.app.models.user import User

def getUserSecurityAuthorities(userId, session=None):

    user = session.query(User).filter(User.id == userId).first()

    authorities = []

    for sg in user.securityGroups:
        for sa in sg.authorities:
            authorities.append(sa)
            
    return authorities




