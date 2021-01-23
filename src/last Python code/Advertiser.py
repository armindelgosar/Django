from BaseAdvertising import BaseAdvertising


class Advertiser(BaseAdvertising):
    _advertisers = []

    def __init__(self, id, name):
        super(Advertiser, self).__init__()
        self._id = id
        self._name = name
        Advertiser._advertisers.append(self)

    def get_name(self):
        return self._name

    def set_name(self, name):
        """it changes the advertiser's name"""
        self._name = name

    @staticmethod
    def help():
        print("This class saves each Advertiser's id, name, clicks and views!")

    @staticmethod
    def describe_me():
        print("This class's responsibility is maintaining system's advertiser's data!")

    @staticmethod
    def getTotalClicks():
        total_clicks = 0
        for advertiser in Advertiser._advertisers:
            total_clicks += advertiser._clicks
        print("--> {}".format(total_clicks))
