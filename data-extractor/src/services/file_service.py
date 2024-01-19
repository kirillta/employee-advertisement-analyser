import json
from json import JSONEncoder
import os


class FileService:
    def read(self, path: str):
        absolute_path: str = self._buildPath(path)

        with open(absolute_path, 'r', encoding=self.ENCODING) as input_file:
            return json.load(input_file)
        
    
    def write(self, path: str, data, encoder=JSONEncoder) -> None:
        absolute_path: str = self._buildPath(path)
        
        with open(absolute_path, "w", encoding=self.ENCODING) as output_file:
            json.dump(data, output_file, cls=encoder, ensure_ascii=False, indent=4)
        
    
    def _buildPath(self, path: str) -> str:
        absolute_path = os.getcwd()
        return os.path.join(absolute_path, path)


    ENCODING = 'UTF8'
