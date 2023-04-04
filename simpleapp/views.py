from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import News1
from .forms import NewsForm
from .filters import News1Filter
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class NewsList(LoginRequiredMixin, ListView):
    raise_exception = True
    model = News1
    ordering = '-data'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 5

class NewsDetail(LoginRequiredMixin, DetailView):
    raise_exception = True
    model = News1
    template_name = 'one_news.html'
    context_object_name = 'one_news'

class NewsCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    raise_exception = True
    permission_required = ('simpleapp.add_product',)
    form_class = NewsForm
    model = News1
    template_name = "news_edit.html"

class Search(LoginRequiredMixin, ListView):
    raise_exception = True
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

class NewsUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('simpleapp.change_product',)
    raise_exception = True
    form_class = NewsForm
    model = News1
    template_name = 'news_edit.html'

class NewsDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ('simpleapp.delete_product',)
    raise_exception = True
    model = News1
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')

