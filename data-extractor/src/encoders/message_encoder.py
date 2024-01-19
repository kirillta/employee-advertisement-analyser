from datetime import datetime
from json import JSONEncoder


class MessageEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        return o.__dict__