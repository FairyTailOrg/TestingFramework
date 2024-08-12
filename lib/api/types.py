from typing import List, Dict, Any, Union
from jsonschema import validate, ValidationError

class JsonSchema:
    def to_dict(self) -> Dict[str, Any]:
        """Convierte la clase en un diccionario que representa el JSON Schema."""
        return self.__dict__

class StringSchema(JsonSchema):
    def __init__(self, format: str = None):
        self.type = "string"
        if format:
            self.format = format

class IntegerSchema(JsonSchema):
    def __init__(self):
        self.type = "integer"

class BooleanSchema(JsonSchema):
    def __init__(self):
        self.type = "boolean"

class ArraySchema(JsonSchema):
    def __init__(self, items: JsonSchema):
        self.type = "array"
        self.items = items.to_dict()

class ObjectSchema(JsonSchema):
    def __init__(self, properties: Dict[str, JsonSchema], required: List[str] = None, additionalProperties: bool = False):
        self.type = "object"
        self.properties = {key: value.to_dict() for key, value in properties.items()}
        self.additionalProperties = additionalProperties
        if required:
            self.required = required
