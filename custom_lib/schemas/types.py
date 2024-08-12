from lib.api.types import ObjectSchema, IntegerSchema, StringSchema, BooleanSchema, ArraySchema

class Example:
    def __init__(self):
        self.integer = IntegerSchema()
        self.string = StringSchema()
        self.boolean = BooleanSchema()
        self.email = StringSchema(format="email")
        self.date = StringSchema(format="date-time")
        self.array = ArraySchema(items=StringSchema())


    def first_example(self):
        return ObjectSchema(
            properties = {
            "id": self.integer,
            "name": self.string,
            "email": self.email,
            "isActive": self.boolean,
            "roles": self.array,
            "createdAt": self.date
        },
        required=["id", "name", "email", "isActive", "roles", "createdAt"]
)