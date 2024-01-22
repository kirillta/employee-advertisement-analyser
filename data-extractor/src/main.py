import os
import sparknlp
import sys
from time import perf_counter
from models.message import Message
from models.stats import Stats
from services.advertisement_service import AdvertisementService
from services.control_message_service import ControlMessageService
from services.file_service import FileService
from services.language_detector import LanguageDetector


def detect_language(spark: sparknlp.SparkSession, messages: list[Message]) -> list[Message]:
    language_detector = LanguageDetector(spark)
    return language_detector.detect(messages)


def get_tg_messages(stats: Stats, file_service: FileService, argv: list[str]) -> tuple[list, Stats]:
    source_file_name = argv[1]
    tg_messages = file_service.read_tg_messages(source_file_name)
    
    stats.source_message_count = len(tg_messages)
    return tg_messages, stats


def process_advertisements(stats: Stats, tg_messages: list) -> tuple[list[Message], Stats]:
    service = AdvertisementService()

    messages = service.get(tg_messages)
    stats.total_advertisement_count = len(messages)

    messages = service.remove_duplicates(messages)
    stats.unique_advertisement_count = len(messages)

    return messages, stats


def process_control_messages(stats: Stats, file_service: FileService, tg_messages: list):
    service = ControlMessageService()
    messages = service.get(tg_messages)
    
    file_service.write_control_messages(messages)

    stats.control_messages_count = len(messages)
    return stats    


def get_spark() -> sparknlp.SparkSession:
    os.environ['PYSPARK_PYTHON'] = sys.executable
    os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
    
    return sparknlp.start()


def main(argv: list[str]):
    stats = Stats()
    
    file_service = FileService()
    tg_messages, stats = get_tg_messages(stats, file_service, argv)

    stats = process_control_messages(stats, file_service, tg_messages)
    advertisements, stats = process_advertisements(stats, tg_messages)

    # spark = get_spark()
    # messages = detect_language(spark, advertisements)

    file_service.write_advertisements(advertisements)
    file_service.write_stats(stats)


time_start = perf_counter()

if __name__ == '__main__':
    main(sys.argv)

time_end = perf_counter()
time_duration = time_end - time_start
print(f'Took {time_duration} seconds')