import json
import os


class FileProvider:
    def read(self, path: str):
        absolute_path: str = self._build_path(path)

        with open(absolute_path, 'r', encoding=self.ENCODING) as input_file:
            return json.load(input_file)
        
    
    def write(self, path, data, encoder=json.JSONEncoder) -> None:
        absolute_path: str = self._build_path(path)
        
        with open(absolute_path, "w", encoding=self.ENCODING) as output_file:
            json.dump(data, output_file, cls=encoder, ensure_ascii=False, indent=4)
        
    
    def _build_path(self, path: str) -> str:
        absolute_path = os.getcwd()
        data_path = self._build_data_path(path)
        return os.path.join(absolute_path, data_path)
    

    def _build_data_path(self, path) -> str:
        return 'data' + os.sep + path


    ENCODING = 'UTF8'
