from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import RedirectView, TemplateView
from rest_framework import generics, authentication
from rest_framework import permissions
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .forms import CreateAd
from .serializers import *


class AdDetailedList(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Ad.objects.all()
    serializer = AdSerializer(queryset, many=True)


class AdList(generics.ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permissions = [IsAdminUser]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = AdSerializer(queryset, many=True)
        return Response(serializer.data)


class ShowAds(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        Ad.inc_all_views(request.ip)
        serializer = AdvertiserSerializer(Advertiser.objects.all(), many=True)
        return Response(serializer.data)


class AdCreate(generics.ListCreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdvertiserManagement(TemplateView):
    template_name = "advertiser_management/advertiser_management.html"

    def get_context_data(self, **kwargs):
        context = {
            "welcome": "This is my first project in Yektanet!", }
        return context


class CreateAdView(View):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    form_class = CreateAd
    initial = {'key': 'value'}
    template_name = 'advertiser_management/make_ad.html'

    def get(self, request, *args, **kwargs):
        form = CreateAd
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            advertiser_id1 = form.cleaned_data.get('advertiser_id')
            image1 = form.cleaned_data.get('image')
            title1 = form.cleaned_data.get('title')
            link1 = form.cleaned_data.get('link')
            Ad.create(title1, link1, image1, Advertiser.objects.get(pk=int(advertiser_id1)))
            return HttpResponseRedirect('ads')

        return render(request, self.template_name, {'form': form})


class AdRedirectView(RedirectView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    pattern_name = 'ad-redirect'
    query_string = False
    ad = ""

    def get_redirect_url(self, *args, **kwargs):
        self.ad = get_object_or_404(Ad, pk=kwargs['pk'])
        return self.ad.link

    def get(self, request, *args, **kwargs):
        self.ad = get_object_or_404(Ad, pk=kwargs['pk'])
        self.ad.inc_clicks(request.ip)
        return super().get(request, *args, **kwargs)
