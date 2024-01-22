from models.message import Message


class MessageTable:
    def __init__(self) -> None:
        self.buckets: dict[str, dict[int, Message]] = dict()
        pass


    def dump_duplicates(self) -> list[list[Message]]:
        results: list[list[Message]] = list()
        
        for bucket in self.buckets.values():
            if len(bucket.values()) < 2:
                continue
            
            values = list(bucket.values())
            results.append(values)

        return results
    

    def set(self, message: Message):
        if message.hash in self.buckets.keys():
            bucket = self.buckets[message.hash]
            bucket[message.id] = message
            
            return
        
        new_bucket = dict()
        new_bucket[message.id] = message

        self.buckets[message.hash] = new_bucket
