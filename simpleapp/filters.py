from django.forms import DateTimeInput
from django_filters import FilterSet, DateTimeFilter

from .models import News1

class News1Filter(FilterSet):

    added_after = DateTimeFilter(
        field_name='data',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT',
            attrs={'type': 'datetime-local'})
    )

    class Meta:
        model = News1

        fields = {

            'title': ['icontains'],
            'content': ['exact']

        }