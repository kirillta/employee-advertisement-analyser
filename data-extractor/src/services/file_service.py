from encoders.message_encoder import MessageEncoder
from encoders.stats_encoder import StatsEncoder
from services.file_provider import FileProvider


class FileService:
    def __init__(self) -> None:
        self.file_provider = FileProvider()


    def read_tg_messages(self, source_file_name: str):
        file_content = self.file_provider.read(source_file_name)
        return file_content['messages']
    

    def write_messages(self, messages):
        self.file_provider.write('results.json', messages, MessageEncoder)


    def write_stats(self, stats):
        self.file_provider.write('stats.json', stats, StatsEncoder)