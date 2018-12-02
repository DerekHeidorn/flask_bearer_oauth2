import string
from random import randint
from random import choice
from random import SystemRandom


def random_user_private_key(max_size):
    all_char = string.ascii_letters + string.digits
    rand = "".join(SystemRandom().choice(all_char) for x in range(max_size))

    return rand


def random_string(min_char, max_char):
    all_char = string.ascii_letters + string.digits
    rand = "".join(choice(all_char) for x in range(randint(min_char, max_char)))

    return rand


def get_user_authorities(user):
    authorities = []

    if user is not None and user.security_groups is not None:
        for sg in user.security_groups:
            if sg is not None:
                for sa in sg.authorities:
                    authorities.append(sa)

    return authorities
