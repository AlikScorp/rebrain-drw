from django.urls import path
from .views import ServerViewSet, ServerDetailView, ServerAddView, ServerViewSetShort, \
    PerfMonLogSet, PerfMonLogAddView, PerfMonDetailView


urlpatterns = [
    path('servers/', ServerViewSet.as_view()),
    path('servers/<int:pk>', ServerDetailView.as_view()),
    path('servers/add', ServerAddView.as_view()),
    path('servers/status/', ServerViewSetShort.as_view()),
    path('perfmon/', PerfMonLogSet.as_view()),
    path('perfmon/<int:pk>', PerfMonDetailView.as_view()),
    path('perfmon/add/', PerfMonLogAddView.as_view()),
]
