from datetime import datetime
from utils.text_normalizer import TextNormalizer
from models.message import Message
from enums.message_type import MessageType


class DataExtractor:
    def __init__(self, normalizer: TextNormalizer) -> None:
        self.normalizer: TextNormalizer = normalizer


    def process(self, tg_messages) -> list[Message]:
        results: list[Message] = []
        for tg_message in tg_messages:
            if tg_message['type'] != 'message':
                continue

            text = tg_message['text']
            message_type = self._get_message_type(text)
            if message_type == None:
                continue
            
            results.append(self._build_message(tg_message, message_type))

        return results
    

    def _build_message(self, tg_message, message_type: MessageType) -> Message:
        normalized_text: str = self.normalizer.normalize(tg_message['text'])
        date = datetime.fromtimestamp(int(tg_message['date_unixtime']))
        
        return Message(tg_message['id'], date, message_type, normalized_text)
    

    def _get_message_type(self, text):
        if self._is_advertisement(text):
            return MessageType.ADVERTISEMENT
        elif self._is_long_message(text):
            return MessageType.PLAIN
        else:
            return None


    def _is_advertisement(self, text) -> bool:
        if not isinstance(text, list):
            return False
        
        for segment in text:
            if isinstance(segment, str):
                continue

            if segment['type'] != 'hashtag':
                continue

            if segment['text'] in self.ADVERTISEMENT_TAGS:
                return True
            
        return False


    def _is_long_message(self, text) -> bool:
        normalized_text = self.normalizer.normalize(text)
        return self.MINIMAL_CONTROL_SAMPLE_MESSAGE_LENGTH <= len(normalized_text)
    

    MINIMAL_CONTROL_SAMPLE_MESSAGE_LENGTH = 1000
    ADVERTISEMENT_TAGS = { '#вакансия' }