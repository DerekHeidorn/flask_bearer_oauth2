

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


def serialize_group_detail(group_details):
    group = serialize_group(group_details.group)

    active_members = []
    for m in group_details.active_members:
        active_members.append(serialize_person(m.person))

    active_managers = []
    for m in group_details.active_managers:
        active_managers.append(serialize_person(m.person))

    return {"group": group, "active_members": active_members, "active_managers": active_managers}


def serialize_codetable(codetable_data):
    data = []
    for item in codetable_data:
        data.append({"code": item.code.strip(), "description": item.description.strip()})
    return data
