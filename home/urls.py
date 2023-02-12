from django.urls import path, include
from . import views

urlpatterns = [
    path('landing-page/', views.landing_page),
    path('testimonials/', views.testimonials),
    path('team-members/', views.teams),
    path('team-members-id/', views.teams_id),
    path('navbar/', views.navbar),
    path('faqs/', views.faq_list),
    path('team-single/<int:id>/', views.teams_single),
]
