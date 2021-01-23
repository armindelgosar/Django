from BaseAdvertising import BaseAdvertising


class Ad(BaseAdvertising):

    def __init__(self, id, title, imgurl, link, advertiser):
        super(Ad, self).__init__()
        self._id = id
        self._title = title
        self._imgUrl = imgurl
        self._link = link
        self._advertiser = advertiser

    def get_title(self):
        return self._title

    def get_imgUrl(self):
        return self._imgUrl

    def set_imgUrl(self, value):
        self._imgUrl = value

    def get_link(self):
        return self._link

    def set_title(self, value):
        self._title = value

    def set_link(self, value):
        self._link = value

    def set_advertiser(self, value):
        self._advertiser = value

    @staticmethod
    def describeMe():
        print("This class's responsibility is maintaining system's advertise's data!")
