import django_filters
from django_filters import FilterSet
from django.forms import DateTimeInput
from .models import Post


class PostFilter(FilterSet):
    dateCreation_gt = django_filters.DateFilter(
        field_name='dateCreation', lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%d',
            attrs={'type':'date'}),
        )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'categoryType': ['exact'],
        }

