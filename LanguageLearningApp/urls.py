from django.contrib import admin
from words.views import WordListView, AddWordView, EditWordView
from django.urls import path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("word_list", WordListView.as_view(), name="word_list"),
    path("", AddWordView.as_view(), name="add_word"),
    path("edit_word/<int:word_id>/", EditWordView.as_view(), name="edit_word"),
]
