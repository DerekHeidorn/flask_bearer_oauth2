from project.app.web.schemas.groupSchemas import GroupSchema, PersonSchema


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


def serialize_membership(membership, user_info=None):

    d = dict()
    if user_info is not None:
        if 'alias' in user_info:
            d['alias'] = user_info['alias']

    d['user_uuid'] = membership.person.user_uuid
    d['membership_from_ts'] = str(membership.from_ts)

    return d


def serialize_manager(manager, user_info=None):

    d = dict()
    if user_info is not None:
        if 'alias' in user_info:
            d['alias'] = user_info['alias']

    d['user_uuid'] = manager.person.user_uuid
    d['manager_from_ts'] = str(manager.from_ts)

    return d


def serialize_group_detail(group_details, user_info=None):
    group = GroupSchema().dump(group_details.group)

    active_members = []
    for m in group_details.active_members:
        user = None
        if user_info:
            for u in user_info:
                print("u=" + str(u))
                if u['user_uuid'] == str(m.person.user_uuid):
                    user = u
                    break
        if user is not None:
            active_members.append({"user_uuid": str(m.person.user_uuid),
                                   "alias": user['alias']})
        else:
            active_members.append(PersonSchema().dump(m.person))

    active_managers = []
    for m in group_details.active_managers:
        user = None
        if user_info:
            for u in user_info:
                if u['user_uuid'] == str(m.person.user_uuid):
                    user = u
                    break
        if user is not None:
            active_managers.append({"user_uuid": str(m.person.user_uuid),
                                    "alias": user['alias']})
        else:
            active_managers.append(PersonSchema().dump(m.person))

    return {"group": group, "active_members": active_members, "active_managers": active_managers}
