from marshmallow import Schema, fields

class BookSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    author = fields.Str(required=True)