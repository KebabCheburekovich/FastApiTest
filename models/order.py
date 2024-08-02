from tortoise import fields
from tortoise.models import Model


class Order(Model):
    id = fields.IntField(pk=True)
    apartment_number = fields.IntField()

    pet = fields.ForeignKeyField('models.Dog', related_name='orders')

    start_at = fields.DatetimeField()

    class Meta:
        table = "order"
