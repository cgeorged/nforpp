from django.urls import path
from n4api import views


urlpatterns = [
    path('', views.parapage, name='paraphrase'),
    path('paraphrase', views.paraphrase_text, name='paraphrase_text')
]