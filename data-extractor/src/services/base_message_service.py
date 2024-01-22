from datetime import datetime
from enums.message_type import MessageType
from models.message import Message


class BaseMessageService:
    def _build_message(self, tg_message, normalized_text: str, message_type: MessageType) -> Message:
        date = datetime.fromtimestamp(int(tg_message['date_unixtime']))
        
        return Message(tg_message['id'], date, message_type, normalized_text)


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
    

    ADVERTISEMENT_TAGS = { '#вакансия' }