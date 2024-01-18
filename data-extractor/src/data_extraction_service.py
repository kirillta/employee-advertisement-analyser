from text_normalizer import TextNormalizer
from message import Message
from message_type import MessageType


class DataExtractionService:
    def __init__(self, normalizer: TextNormalizer) -> None:
        self.normalizer = normalizer


    def prepare_messages(self, messages):
        results = []
        for message in messages:
            if message['type'] != 'message':
                continue

            text = message['text']
            
            message_type = None
            if self._is_advertisement(text):
                message_type = MessageType.ADVERTISEMENT
            elif self._is_long_message(text):
                message_type = MessageType.PLAIN
            else:
                continue
            
            normalized_text: str = self.normalizer.normalize(text)
            results.append(Message(message['id'], normalized_text, message_type))

        return results


    def _is_advertisement(self, text) -> bool:
        if not isinstance(text, list):
            return False
        
        for segment in text:
            if isinstance(segment, str):
                continue

            if segment['type'] == 'hashtag' and segment['text'] == '#вакансия':
                return True
            
        return False


    def _is_long_message(self, text) -> bool:
        if isinstance(text, str):
            return DataExtractionService.average_message_length <= len(text)
        
        normalized_text = self.normalizer.normalize(text)
        return DataExtractionService.average_message_length <= len(normalized_text)
    

    average_message_length = 1000