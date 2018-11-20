

def generate_response_wrapper(data,
                              global_info_msgs=None,
                              global_warning_msgs=None,
                              global_error_msgs=None,
                              field_error_msgs=None):
    return {
       'data': data,
       'global_info_msgs': global_info_msgs,
       'global_warning_msgs': global_warning_msgs,
       'global_error_msgs': global_error_msgs,
       'field_error_msgs': field_error_msgs
    }


def serialize_group(group):
    return {"group_uuid": group.group_uuid, "group_name": group.group_name}


def serialize_person(person):
    return {"user_uuid": person.user_uuid, "nick_name": person.nick_name}


def serialize_group_detail(group_details, user_info=None):
    group = serialize_group(group_details.group)

    active_members = []
    for m in group_details.active_members:
        user = None
        if user_info:
            for u in user_info:
                print("u=" + str(u))
                if u.user_uuid == m.person.user_uuid:
                    user = u
                    break
        if user is not None:
            active_members.append({"user_uuid": m.person.user_uuid,
                                   "nick_name": m.person.nick_name,
                                   "first_name": user['first_name'],
                                   "last_name": user['last_name']})
        else:
            active_members.append(serialize_person(m.person))

    active_managers = []
    for m in group_details.active_managers:
        user = None
        if user_info:
            for u in user_info:
                if u.user_uuid == m.person.user_uuid:
                    user = u
                    break
        if user is not None:
            active_managers.append({"user_uuid": m.person.user_uuid,
                                    "nick_name": m.person.nick_name,
                                    "first_name": user['first_name'],
                                    "last_name": user['last_name']})
        else:
            active_managers.append(serialize_person(m.person))

    return {"group": group, "active_members": active_members, "active_managers": active_managers}



def serialize_codetable(codetable_data):
    data = []
    for item in codetable_data:
        data.append({"code": item.code.strip(), "description": item.description.strip()})
    return data
