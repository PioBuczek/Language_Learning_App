from django.contrib import admin
from words.views import WordListView, AddWordView
from django.urls import path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("word_list", WordListView.as_view(), name="word_list"),
    path("", AddWordView.as_view(), name="add_word"),
]
