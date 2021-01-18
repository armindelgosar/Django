from BaseAdvertising import BaseAdvertising


class Advertiser(BaseAdvertising):
    advertisers = []

    def __init__(self, id, name):
        self._id = id
        self.name = name
        Advertiser.advertisers.append(self)

    @staticmethod
    def help():
        print("This class saves each Advertiser's id, name, clicks and views!")

    def describeMe(self):
        print("This class's responsibility is maintaining system's advertiser's data!")

    @staticmethod
    def getTotalClicks():
        for i in Advertiser.advertisers:
            print(Advertiser.__getattribute__(i, "name"),
                  Advertiser.__getattribute__(i, "clicks"))
