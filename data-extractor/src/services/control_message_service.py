from enums.message_type import MessageType
from models.message import Message
from services.base_message_service import BaseMessageService
from utils.text_normalizer import TextNormalizer


class ControlMessageService(BaseMessageService):
    def __init__(self) -> None:
        pass


    def get(self, tg_messages) -> list[Message]:
        results: list[Message] = []

        for tg_message in tg_messages:
            if tg_message['type'] != 'message':
                continue

            if self._is_advertisement(tg_message['text']):
                continue

            normalized_text = TextNormalizer.normalize(tg_message['text'])
            if self._is_long_message(normalized_text):
                results.append(self._build_message(tg_message, normalized_text, MessageType.PLAIN))

        return results
    

    def _is_long_message(self, text) -> bool:
        return self.MINIMAL_CONTROL_SAMPLE_MESSAGE_LENGTH <= len(text)
    

    MINIMAL_CONTROL_SAMPLE_MESSAGE_LENGTH = 1000