# filters.py

import django
import django_filters
from .models import BlogPost

class BlogPostFilterSet(django_filters.FilterSet):
    class Meta:
        model = BlogPost
        fields = ['tags', 'other_fields']

        # Override filter for TaggableManager field
        filter_overrides = {
            django.contrib.postgres.fields.ArrayField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
            django.contrib.postgres.fields.JSONField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
            # Add more overrides if needed
        }
