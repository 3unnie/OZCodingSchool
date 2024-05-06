from marshmallow import Schema, fields

#각 모델들의 스키마 정의(검증)/데이터 검증과 직렬화에 사용
class ItemSchema(Schema):
    id = fields.Int(dumy_only=True)
    name = fields.Str(required=True)
    description = fields.Str()