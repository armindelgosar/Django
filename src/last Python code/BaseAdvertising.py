
class BaseAdvertising:

    def __init__(self):
        self._clicks = 0
        self._views = 0

    def get_clicks(self):
        return self._clicks

    def get_views(self):
        return self._views

    def inc_views(self):
        self._views += 1

    def inc_clicks(self):
        self._clicks += 1

    @staticmethod
    def describe_me():
        print("nothing!")
