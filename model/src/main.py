from data_preparation_service import DataPreparationService
from file_service import FileService
from text_normalizer import TextNormalizer
from message_encoder import MessageEncoder
import os


input_file_path = 'dist' + os.sep + 'unprocessed_set.json'
output_file_path = 'dist' + os.sep + 'processed_set.json'


file_service = FileService()
file_content = file_service.read(input_file_path)
messages = file_content['messages']

text_normalizer = TextNormalizer()
data_preparation_service = DataPreparationService(text_normalizer)

results = data_preparation_service.prepare_messages(messages)

file_service.write(output_file_path, results, MessageEncoder)