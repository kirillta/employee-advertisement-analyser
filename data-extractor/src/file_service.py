import json
from json import JSONEncoder
import os


class FileService:
    def read(self, path):
        absolute_path = self._buildPath(path)

        with open(absolute_path, 'r', encoding=FileService.encoding) as input_file:
            return json.load(input_file)
        
    
    def write(self, path, data, encoder=JSONEncoder):
        absolute_path = self._buildPath(path)
        
        with open(absolute_path, "w", encoding=FileService.encoding) as output_file:
            json.dump(data, output_file, cls=encoder, ensure_ascii=False)
        
    
    def _buildPath(self, path: str) -> str:
        absolute_path = os.getcwd()
        parent_directory = os.path.join(absolute_path, os.pardir)
        return os.path.join(absolute_path, path)


    encoding = 'UTF8'
