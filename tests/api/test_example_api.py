from custom_lib.schemas.types import Example
from lib.api.api_lib import SchemaValidator
import pytest


class TestApiExample:
    def setup_method(self):
        self.example = Example()
        self.validator = SchemaValidator()

    def test_api_example(self):
        user_schema = self.example.first_example()
        # Replace this by the real request.
        response_data = {
            "id": 123,
            "name": "John Doe",
            "email": "johndoe@example.com",
            "isActive": True,
            "roles": ["admin", "user"],
            "createdAt": "2024-08-06T12:00:00Z"
        }
        assert self.validator.validate(response_data, user_schema)
