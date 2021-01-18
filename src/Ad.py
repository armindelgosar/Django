from BaseAdvertising import BaseAdvertising


class Ad(BaseAdvertising):

    def __init__(self, id, title, imgurl, link, advertiser):
        self._id = id
        self._title = title
        self._imgUrl = imgurl
        self._link = link
        self._advertiser = advertiser

    @staticmethod
    def describeMe():
        print("This class's responsibility is maintaining system's advertise's data!")
