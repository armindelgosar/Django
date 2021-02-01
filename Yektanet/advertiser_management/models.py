from django.db import models


class BaseAdvertising(models.Model):
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)


class Advertiser(BaseAdvertising):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.id)

    @staticmethod
    def getChoiceList():
        list1 = []
        for advertiser in Advertiser.objects.all():
            list1.append((advertiser.id, advertiser.name + " id: " + str(advertiser.id)))
        return list1

    @staticmethod
    def get_by_id(id):
        for advertiser in Advertiser.objects.all():
            if advertiser.id == id:
                return advertiser


class Ad(BaseAdvertising):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images", default="")
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)