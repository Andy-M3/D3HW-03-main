from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import News1
from .forms import NewsForm
from .filters import News1Filter
from django.urls import reverse_lazy


class NewsList(ListView):
    model = News1
    ordering = '-data'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 5

class NewsDetail(DetailView):
    model = News1
    template_name = 'one_news.html'
    context_object_name = 'one_news'

class NewsCreate(CreateView):
    form_class = NewsForm
    model = News1
    template_name = "news_edit.html"

class Search(ListView):
    model = News1
    template_name = 'search.html'
    context_object_name = 'news'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = News1Filter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = \
            datetime.utcnow()
        context['next_info'] = None
        context['filterset'] = self.filterset
        return context

class NewsUpdate(UpdateView):
    form_class = NewsForm
    model = News1
    template_name = 'news_edit.html'

class NewsDelete(DeleteView):
    model = News1
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')

