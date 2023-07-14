from django.urls import path
from .views import *

urlpatterns = [
    path('', VlogListView.as_view(), name='home'),
    path('post/<int:pk>/', VlogDetailView.as_view(), name='post'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('services/', Services, name='services'),
    path('partifolio/', Partfifolio, name='partifolio'),
    path('section/', Section, name='section'),
    path('question/', Question, name='question'),
    path('pricing/', Pricing, name='pricing'),
    path('services/', Services, name='services'),

]

