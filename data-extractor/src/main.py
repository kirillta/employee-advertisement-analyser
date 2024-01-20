import os
import sparknlp
import sys
from models.message import Message
from services.data_extractor import DataExtractor
from services.file_service import FileService
from services.language_detector import LanguageDetector
from utils.text_normalizer import TextNormalizer
from encoders.message_encoder import MessageEncoder


def detect_language(spark: sparknlp.SparkSession, messages: list[Message]) -> list[Message]:
    language_detector = LanguageDetector(spark)
    return language_detector.detect(messages)


def get_messages(tg_messages) -> list[Message]:
    text_normalizer = TextNormalizer()
    data_extractor = DataExtractor(text_normalizer)
    
    return data_extractor.process(tg_messages)


def get_spark() -> sparknlp.SparkSession:
    os.environ['PYSPARK_PYTHON'] = sys.executable
    os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
    
    return sparknlp.start()


def get_tg_messages(file_service, path):
    file_content = file_service.read(path)
    return file_content['messages']


file_service = FileService()
tg_messages = get_tg_messages(file_service, sys.argv[1])
messages = get_messages(tg_messages)

spark = get_spark()
messages = detect_language(spark, messages)

file_service.write(messages, sys.argv[2], MessageEncoder)