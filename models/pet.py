from tortoise import Model, fields


class Dog(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)
    breed = fields.CharField(max_length=50)

    class Meta:
        table = "dog"
