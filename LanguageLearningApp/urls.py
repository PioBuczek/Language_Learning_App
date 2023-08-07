from django.contrib import admin
from words.views import word_list, add_word
from django.urls import path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", word_list, name="word_list"),
    path("add_word/", add_word, name="add_word"),
]
