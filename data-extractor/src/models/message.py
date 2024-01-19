from datetime import datetime
from enums.message_type import MessageType


class Message:
    def __init__(self, id: int, date: datetime, type: MessageType, content: str) -> None:
        self.id: int = id
        self.date: datetime = date
        self.type: MessageType = type
        self.content: str = content
        