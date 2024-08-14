import json
import os


class Types:
    def convert_json_to_dict(self, filepath):
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
    def __init__(self):
        self.appt_reasons = self.convert_json_to_dict("/scheduling/appt_reasons.json")

class Content(Types):
    def __init__(self):
        pass