

def serialize_group(group):
    return {"group_uuid": group.group_uuid, "group_name": group.group_name}


def serialize_codetable(codetable_data):
    data = []
    for item in codetable_data:
        data.append({"code": item.code.strip(), "description": item.description.strip()})
    return data
