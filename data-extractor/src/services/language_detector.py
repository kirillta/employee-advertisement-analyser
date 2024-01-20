import sparknlp
from sparknlp.base import DocumentAssembler, Pipeline
from sparknlp.annotator import LanguageDetectorDL, SentenceDetector
from models.message import Message


class LanguageDetector:
    def __init__(self, spark: sparknlp.SparkSession) -> None:
        self.spark: sparknlp.SparkSession = spark
        

    def detect(self, messages: list[Message]) -> list[Message]:
        data_frame = self._get_data_frames(messages)
        nlp_pipeline = self._get_nlp_pipeline()

        result_frame = nlp_pipeline.fit(data_frame).transform(data_frame)
        return self._to_list(result_frame, messages)
    

    def _get_data_frames(self, messages: list[Message]):
        data = []
        for message in messages:
            data.append([message.id, message.content])

        return self.spark.createDataFrame(data, ['id', 'text'])
    

    def _get_nlp_pipeline(self):
        document_assembler = DocumentAssembler() \
            .setInputCol('text') \
            .setOutputCol('document')

        sentence_detector = SentenceDetector() \
            .setInputCols('document') \
            .setOutputCol('sentence')

        language_detector = LanguageDetectorDL.pretrained('ld_wiki_tatoeba_cnn_220', 'xx') \
            .setInputCols('sentence') \
            .setOutputCol('language') 

        return Pipeline(stages=[document_assembler, sentence_detector, language_detector])
    

    def _to_dict(self, messages: list[Message]) -> dict[int, Message]:
        results: dict[int, Message] = {}
        for message in messages:
            results[message.id] = message
        
        return results
    

    def _to_list(self, result_frame, messages: list[Message]) -> list[Message]:
        message_dictionary: dict[int, Message] = self._to_dict(messages)

        for row in result_frame.select('id', 'language.result').collect():
            message: Message | None = message_dictionary.get(row[0])
            if message is None:
                continue
            
            message.language = row[1][0]

        return list(message_dictionary.values())