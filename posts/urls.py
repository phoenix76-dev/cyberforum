from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url('id/(?P<question_id>)', QuestionView.as_view(), name='detail'),
    url('node/(?P<section_url>)', SectionView.as_view(), name='section'),
    url('^', IndexPageView.as_view(), name='index')
]