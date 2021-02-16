from django.db import models
from django.utils import timezone
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class BaseAdvertising(models.Model):
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    class Meta:
        abstract = True


class Advertiser(BaseAdvertising):
    name = models.CharField(max_length=20)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.id)

    def inc_views(self):
        self.views += 1
        self.save()

    def inc_clicks(self):
        self.clicks += 1
        self.save()

    @staticmethod
    def getChoiceList():
        list1 = list((Advertiser.id, "{} id: {}".format(Advertiser.name, str(Advertiser.id))))
        return list1

    @staticmethod
    def get_by_id(id):
        for advertiser in Advertiser.objects.all():
            if advertiser.id == id:
                return advertiser


class Ad(BaseAdvertising):
    APPROVE_CHOICES = (
        ('a', 'APPROVED'),
        ('d', 'Disapproved'),
        ('n', 'Not checked')
    )
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    link = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images", default="")
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE, related_name='ads')
    approve = models.CharField(max_length=1, choices=APPROVE_CHOICES, default='n')

    @property
    def views(self):
        views = len(View.objects.filter(ad=self))
        return views

    @property
    def clicks(self):
        clicks = len(Click.objects.filter(ad=self))
        return clicks

    def __str__(self):
        return str(self.id)

    @classmethod
    def create(cls, title, link, image, advertiser):
        ad = cls(title=title, link=link, image=image, advertiser=advertiser)
        ad.save()
        return ad

    @staticmethod
    def inc_all_views(ip):
        for ad in Ad.objects.all():
            if ad.approve == 'a':
                ad.inc_views(ip)

    def show_views(self):
        views = View.objects.filter(ad=self)
        for v in views:
            print('{}  {}  {}'.format(v.ad, v.date, v.ip))

    def make_daily_views(self):
        set1 = ViewsPerHour.objects.filter(ad=self, start_time__day=timezone.now().day - 1)
        count = 0
        for ob in set1:
            count += ob.content
        views_per_day = ViewsPerDay.objects.create(ad=self,
                                                   start_time=timezone.now().replace(day=timezone.now().day - 1, hour=0,
                                                                                     minute=0, second=0,
                                                                                     microsecond=0),
                                                   end_time=timezone.now().replace(day=timezone.now().day, hour=0,
                                                                                   minute=0, second=0,
                                                                                   microsecond=0),
                                                   content=count)
        views_per_day.save()

    def make_daily_clicks(self):
        set1 = ClicksPerHour.objects.filter(ad=self, start_time__day=timezone.now().day - 1)
        count = 0
        for ob in set1:
            count += ob.content
        click_per_day = ClicksPerHour.objects.create(ad=self,
                                                     start_time=timezone.now().replace(hour=timezone.now().hour - 1,
                                                                                       minute=0, second=0,
                                                                                       microsecond=0),
                                                     end_time=timezone.now().replace(hour=timezone.now().hour,
                                                                                     minute=0, second=0,
                                                                                     microsecond=0),
                                                     content=count)
        click_per_day.save()

    def make_hourly_views(self):
        count = len(View.objects.filter(ad=self, date__hour=timezone.now().hour-1, date__date=timezone.now()))
        view_per_hour = ViewsPerHour.objects.create(ad=self,
                                                    start_time=timezone.now().replace(hour=timezone.now().hour - 1,
                                                                                      minute=0, second=0,
                                                                                      microsecond=0),
                                                    end_time=timezone.now().replace(hour=timezone.now().hour,
                                                                                    minute=0, second=0,
                                                                                    microsecond=0),
                                                    content=count)
        view_per_hour.save()

    def make_hourly_clicks(self):
        count = len(Click.objects.filter(ad=self, date__hour=timezone.now().hour-1, date__date=timezone.now()))
        click_per_hour = ClicksPerHour.objects.create(ad=self,
                                                      start_time=timezone.now().replace(hour=timezone.now().hour - 1,
                                                                                        minute=0, second=0,
                                                                                        microsecond=0),
                                                      end_time=timezone.now().replace(hour=timezone.now().hour,
                                                                                      minute=0, second=0,
                                                                                      microsecond=0),
                                                      content=count)
        click_per_hour.save()

    def inc_views(self, ip):
        view = View.objects.create(ip=ip, ad=self)
        self.advertiser.inc_views()
        view.save()

    def inc_clicks(self, ip):
        click = Click.objects.create(ip=ip, ad=self)
        self.advertiser.inc_clicks()
        click.save()


class ClicksPerHour(models.Model):
    ad = models.ForeignKey(to=Ad, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    content = models.IntegerField(default=0)


class ViewsPerHour(models.Model):
    ad = models.ForeignKey(to=Ad, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    content = models.IntegerField(default=0)

    # @staticmethod
    # def show_detail(ad):
    #     x = ViewsPerHour.objects.filter(ad=ad)
    #     for a in x:
    #         print('{} {} {} {}'.format(a.ad, a.start_time, a.end_time, a.content))


class ClicksPerDay(models.Model):
    ad = models.ForeignKey(to=Ad, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    content = models.IntegerField(default=0)

    # @staticmethod
    # def show_detail(ad):
    #     x = ClicksPerDay.objects.filter(ad=ad)
    #     for a in x:
    #         print('{} {} {} {}'.format(a.ad, a.start_time, a.end_time, a.content))


class ViewsPerDay(models.Model):
    ad = models.ForeignKey(to=Ad, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    content = models.IntegerField(default=0)

    # @staticmethod
    # def show_detail(ad):
    #     x = ViewsPerDay.objects.filter(ad=ad)
    #     for a in x:
    #         print('{} {} {} {}'.format(a.ad, a.start_time, a.end_time, a.content))


class View(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    ip = models.TextField(null=False)
    date = models.DateTimeField(default=timezone.now)


class Click(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    ip = models.TextField(null=False)
    date = models.DateTimeField(default=timezone.now)
