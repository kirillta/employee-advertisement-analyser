from enums.message_type import MessageType


class Message:
    def __init__(self, id: int, content: str, type: MessageType) -> None:
        self.content: str = content
        self.id: int = id
        self.type: MessageType = type