from BaseAdvertising import BaseAdvertising
from Ad import Ad
from Advertiser import Advertiser

baseAdvertising = BaseAdvertising()
advertiser1 = Advertiser(1, "name1")
advertiser2 = Advertiser(2, "name2")
ad1 = Ad(1, "title1", "img-url1", "link1", advertiser1)
ad2 = Ad(2, "title2", "img-url2", "link2", advertiser2)
baseAdvertising.describeMe()
ad2.describeMe()
advertiser1.describeMe()
ad1.incViews()
ad1.incViews()
ad1.incViews()
ad1.incViews()
ad2.incViews()
ad1.incClicks()
ad1.incClicks()
ad2.incClicks()
Advertiser.__getattribute__(advertiser2, "name")
Advertiser.__setattr__(advertiser2, "name", "new name")
Advertiser.__getattribute__(advertiser2, "name")
Ad.__getattribute__(ad1, "clicks")
Advertiser.__getattribute__(advertiser2, "clicks")
Advertiser.getTotalClicks()
Advertiser.help()
