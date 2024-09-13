"""File with all the generic api libraries."""
from jsonschema import ValidationError, validate

from lib.logger_config import logger


class SchemaValidator:
    """This class will validate the schemas received."""

    def __init__(self) -> None:
        """Initialize the useful methods or class."""
        self.logger = logger

    def validate(self, instance: dict, schema):
        """Validate the response or dict vs the json schema specified.

        Args:
            instance (dict): Response of a endpoint.
            schema (_type_): json schema converted to dict.

        Returns:
            boolean: True if match.
        """
        try:
            validate(instance=instance, schema=schema)
            self.logger.info("Instance correctly validated.")
        except ValidationError as e:
            self.logger.error("Error:", e.message)
            return False
        return True
