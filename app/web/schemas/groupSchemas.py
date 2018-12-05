from marshmallow import fields, Schema
from app.services.utils import sha256


class GroupSchema(Schema):
    group_uuid = fields.String(required=True)
    group_name = fields.String(required=True)
    group_de = fields.String(required=True)

    group_uuid_digest = fields.Method('get_digest')

    subscribed = fields.Boolean()

    def get_digest(self, obj):
        if obj.group_uuid is not None:
            return sha256.hexdigest(str(obj.group_uuid))
        return None


class PersonSchema(Schema):
    user_uuid = fields.String(required=True)


class MembershipSchema(Schema):
    user_uuid = fields.String(required=True)
    from_ts = fields.String()
