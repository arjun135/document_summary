from django.urls import path
from django.views.generic import TemplateView

from summarizer import views


urlpatterns = [
    path('', views.index, name='index'),
    path('summarize_page', views.summarize_page, name='summarize_page'),
    path('summarize_hindi_page', views.summarize_hindi_page, name='summarize_hindi_page'),
    path('save_summary', views.save_summary, name='save_summary'),
    path('history', views.history, name='history'),
    path('history_topic', views.history_topic, name='history_topic'),
    path('Hindi', TemplateView.as_view(template_name='summarizer/Hindi.html'), name='Hindi'),  # ---
]
