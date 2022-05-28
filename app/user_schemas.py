from marshmallow import Schema, fields
from marshmallow.validate import Length


class UserSchema(Schema):
    class Meta:
        fields = ('username', 'name')


class ParamsUserSchema(Schema):
    username = fields.Str(required=True, validate=Length(max=255))
    name = fields.Str(required=True, validate=Length(max=255))
    password = fields.Str(required=True, validate=Length(max=255))

user_schema = UserSchema()
params_user_schema = ParamsUserSchema()

