from marshmallow import fields, Schema


class GroupSchema(Schema):
    group_uuid = fields.String(required=True)
    group_name = fields.String(required=True)
    group_de = fields.String(required=True)


class PersonSchema(Schema):
    user_uuid = fields.String(required=True)
    nick_name = fields.String(required=True)


class MembershipSchema(Schema):
    user_uuid = fields.String(required=True)
    nick_name = fields.String(required=True)
