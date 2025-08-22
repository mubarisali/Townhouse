from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = "villas"

urlpatterns = [
    path('', views.home, name='home'),
    path('location/', views.location, name='location'),
    path('overview/', views.overview, name='overview'),
    path('gallery/', views.gallery, name='gallery'),
    path('amenities/', views.amenities, name='amenities'),
    path('payment-plan/', views.payment_plan, name='payment_plan'),
     path("lead-submit/", views.lead_submit, name="lead_submit"),          # optional handlers
    path("callback-submit/", views.callback_submit, name="callback_submit"),
    path('contact/', views.contact, name='contact'),
    path("api/web3forms/", views.web3forms_webhook, name="web3forms_webhook"),

]
