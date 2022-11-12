from marshmallow import fields


class BaseSchemaMixin:
    id = fields.Integer(dump_only=True)
