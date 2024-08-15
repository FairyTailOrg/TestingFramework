# jsonschema_lib/validator.py

from jsonschema import ValidationError, validate

from lib.logger_config import setup_logger


class SchemaValidator:
    def __init__(self) -> None:
        self.logger = setup_logger()

    def validate(self, instance: dict, schema):
        try:
            validate(instance=instance, schema=schema)
            self.logger.info("Instance correctly validated")
        except ValidationError as e:
            self.logger.error("Error:", e.message)
            return False
        return True
