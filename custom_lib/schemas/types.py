"""File to manage and use the schemas instanced."""
import json
import os


class Types:
    """Useful tools to json schema validation."""

    def convert_json_to_dict(self, filepath):
        """Get a json file and convert it to schema.

        Args:
            filepath (str): path of the json file.

        Raises:
            FileNotFoundError: When file was not found.
            ValueError: When the file is not a valid file.

        Returns:
            dict: The json file to dict.
        """
        file_path = "custom_lib/schemas" + filepath
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"El archivo {file_path} no existe.")

        with open(file_path, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError as e:
                raise ValueError(f"Error al decodificar JSON: {e}")

        return data


class Scheduling(Types):
    """Initialize the scheduling api schemas.

    Args:
        Types (class): use the types schema validator functions.
    """

    def __init__(self):
        """Get all the schemas and instance them here."""
        self.appt_reasons = self.convert_json_to_dict(
            "/scheduling/appt_reasons.json"
            )


class Content(Types):
    """Initialize the content managment api schemas.

    Args:
        Types (class): use the types schema validator functions.
    """

    def __init__(self):
        """Get all the schemas and instance them here."""
        pass
