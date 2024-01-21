import os
import sparknlp
import sys
from time import perf_counter
from models.message import Message
from models.stats import Stats
from services.advertisement_service import AdvertisementService
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


def get_spark() -> sparknlp.SparkSession:
    os.environ['PYSPARK_PYTHON'] = sys.executable
    os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
    
    return sparknlp.start()


def main(argv: list[str]):
    stats = Stats()
    
    file_service = FileService()
    tg_messages, stats = get_tg_messages(stats, file_service, argv)
    
    advertisement_service = AdvertisementService()
    total_advertisements = advertisement_service.process(tg_messages)
    stats.total_advertisement_count = len(total_advertisements)

    # spark = get_spark()
    # messages = detect_language(spark, messages)

    file_service.write_messages(total_advertisements)
    file_service.write_stats(stats)


time_start = perf_counter()

if __name__ == '__main__':
    main(sys.argv)

time_end = perf_counter()
time_duration = time_end - time_start
print(f'Took {time_duration} seconds')