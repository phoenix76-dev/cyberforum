from django.shortcuts import render_to_response, get_object_or_404
from django.http.response import HttpResponse
from django.views.generic import ListView, DetailView
from .models import *


class IndexPageView(ListView):
    template_name = 'forum/index.html'
    context_object_name = 'root_elements'
    queryset = Section.objects.filter(has_parent=False).order_by('id')


class SectionView(DetailView):
    template_name = 'forum/section_view.html'
    context_object_name = 'node'
    pk_url_kwarg = 'section_url'

    def get_object(self, **kwargs):
        path_nodes = self.pk_url_kwarg.split('/').remove('')
        result = Section.objects.get(url_name=path_nodes[0])
        for node_name in path_nodes[1:]:
            result = result.subsections.get(url_name=node_name)
        return result


class QuestionView(DetailView):
    template_name = 'forum/question_view.html'
    context_object_name = 'question'
    pk_url_kwarg = 'question_id'

    model = Question


def index(request):
    return HttpResponse('<p>This is main page</p>', content_type='text/html')
