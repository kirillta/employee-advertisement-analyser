from enums.message_type import MessageType
from models.message import Message
from services.base_message_service import BaseMessageService
from structures.message_table import MessageTable
from utils.text_normalizer import TextNormalizer


class AdvertisementService(BaseMessageService):
    def __init__(self) -> None:
        pass


    def get(self, tg_messages) -> list[Message]:
        results: list[Message] = []

        for tg_message in tg_messages:
            if tg_message['type'] != 'message':
                continue

            normalized_text = TextNormalizer.normalize(tg_message['text'])
            if self._is_advertisement(tg_message['text']):
                results.append(self._build_message(tg_message, normalized_text, MessageType.ADVERTISEMENT))

        return results
    

    def remove_duplicates(self, messages: list[Message]) -> list[Message]:
        results: list[Message] = []

        message_table = MessageTable()
        for message in messages:
            message_table.set(message)
        
        duplicates = message_table.dump_duplicates()
        for duplicate_list in duplicates:
            print('\n')
            for duplicate in duplicate_list:
                print(duplicate.hash)

            print('\n')

        return messages