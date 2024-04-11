import json
from datetime import date, datetime

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime) or isinstance(obj, date):
            return obj.timestamp()
        return json.JSONEncoder.default(self, obj)