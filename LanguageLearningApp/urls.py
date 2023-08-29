from django.contrib import admin
from words.views import (
    WordListView,
    AddWordView,
    EditWordView,
    EditWordListView,
    DeleteWord,
    AddGroupView,
    QuizView,
    QuizCheckView,
    QuizStartView,
)
from django.urls import path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("word_list", WordListView.as_view(), name="word_list"),
    path("", AddWordView.as_view(), name="add_word"),
    path("edit_word/<int:word_id>/", EditWordView.as_view(), name="edit_word"),
    path("edit_word_list/", EditWordListView.as_view(), name="edit_word_list"),
    path("delete_word/<int:word_id>", DeleteWord.as_view(), name="delete_word"),
    path("add_group/", AddGroupView.as_view(), name="add_group"),
    path("quiz/", QuizView.as_view(), name="quiz"),
    path("quiz/start/", QuizStartView.as_view(), name="quiz_start"),
    path("quiz/check/", QuizCheckView.as_view(), name="quiz_check"),
]
