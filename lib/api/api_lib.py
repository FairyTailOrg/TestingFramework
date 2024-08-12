# jsonschema_lib/validator.py

from jsonschema import validate, ValidationError
from .types import JsonSchema
from lib.logger_config import setup_logger
import requests

class SchemaValidator:
    def __init__(self) -> None:
        self.logger = setup_logger()

    def validate(self, instance: dict, schema: JsonSchema):
        schema_dict = schema.to_dict()
        try:
            validate(instance=instance, schema=schema_dict)
            self.logger.info("Instance correctly validated")
        except ValidationError as e:
            self.logger.error("Error:", e.message)
            return False
        return True
    