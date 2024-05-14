# from django.shortcuts import render

# # Create your views here.
# # logs/views.py
# from rest_framework import generics, filters
# from django_filters import rest_framework as filters
# from .models import Log
# from .serializers import LogSerializer

# class LogCreateView(generics.CreateAPIView):
#     queryset = Log.objects.all()
#     serializer_class = LogSerializer

# class LogListView(generics.ListAPIView):
#     queryset = Log.objects.all()
#     serializer_class = LogSerializer
#     filter_backends = [filters.CharFilter, filters.OrderingFilter]
#     search_fields = ['level', 'log_string', 'source']
#     ordering_fields = ['timestamp']


# class LogFilter(filters.FilterSet):
#     start_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='gte')
#     end_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='lte')

#     class Meta:
#         model = Log
#         fields = ['level', 'log_string', 'source', 'timestamp']

# class LogListView(generics.ListAPIView):
#     queryset = Log.objects.all()
#     serializer_class = LogSerializer
#     filter_backends = [filters.DjangoFilterBackend, filters.CharFilter, filters.OrderingFilter]
#     filterset_class = LogFilter
#     search_fields = ['level', 'log_string', 'source']
#     ordering_fields = ['timestamp']





# logs/views.py
from rest_framework import generics, filters as drf_filters
from django_filters import rest_framework as django_filters
from .models import Log
from .serializers import LogSerializer

class LogCreateView(generics.CreateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

class LogFilter(django_filters.FilterSet):
    start_date = django_filters.DateTimeFilter(field_name="timestamp", lookup_expr='gte')
    end_date = django_filters.DateTimeFilter(field_name="timestamp", lookup_expr='lte')

    class Meta:
        model = Log
        fields = ['level', 'log_string', 'source', 'timestamp']

class LogListView(generics.ListAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    filter_backends = [django_filters.DjangoFilterBackend, drf_filters.SearchFilter, drf_filters.OrderingFilter]
    filterset_class = LogFilter
    search_fields = ['level', 'log_string', 'source']
    ordering_fields = ['timestamp']

