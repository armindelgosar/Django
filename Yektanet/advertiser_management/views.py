from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .forms import MakeAd
from .models import Advertiser, Ad
from django.views.generic.base import RedirectView


def index(request):
    text = "This is my first django project in Yektanet!"
    return HttpResponse(text)


def make_ad(request):
    if request.method == 'POST':
        form = MakeAd(request.POST)
        if form.is_valid():
            advertiser_id = form.cleaned_data['advertiser_id']
            image = form.cleaned_data['image']
            title = form.cleaned_data['title']
            link = form.cleaned_data['link']
            Ad.objects.create(title=title, link=link, image=image,
                              advertiser_id=advertiser_id)
        else:
            raise Http404("form is invalid!")
    form = MakeAd()
    return render(request, "advertiser_management/make_ad.html", {'form': form})


def show_message(request):
    class OtherAdvertiser:
        def __init__(self, name, id, clicks, views, ads):
            self.name = name
            self.id = id
            self.clicks = clicks
            self.views = views
            self.ads = ads

    advertisers = []
    for advertiser in Advertiser.objects.all():
        list_of_ads = inc_views(advertiser)
        advertisers.append(
            OtherAdvertiser(advertiser.name, advertiser.id, advertiser.clicks, advertiser.views, list_of_ads))
    context = {
        "advertisers": advertisers,
    }
    return render(request, "advertiser_management/ads.html", context)


def inc_views(advertiser):
    ads_list = Ad.objects.filter(advertiser_id=advertiser.id)
    for ad in ads_list:
        ad.views += 1
    advertiser.views += len(ads_list)
    return ads_list

class AdRedirectView(RedirectView):
    pattern_name = 'ad-redirect'
    query_string = False

    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['pk'])
        ad.inc_clicks()
        return ad.link