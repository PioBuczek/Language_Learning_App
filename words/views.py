from django.shortcuts import render, redirect
from .models import Word
from django.views import View


class WordListView(View):
    template = "word_list.html"

    def get(self, request):
        words = Word.objects.all()
        return render(request, self.template, {"words": words})


class AddWordView(View):
    template = "add_word.html"

    def get(self, request):
        message = "Input another word and translation"
        words_for_edit = Word.objects.all()

        if words_for_edit.exists():
            first_word = words_for_edit.first()
        else:
            first_word = None

        return render(
            request, self.template, {"message": message, "first_word": first_word}
        )

    def post(self, request):
        word = request.POST.get("word")
        translation = request.POST.get("translation")
        Word.objects.create(word=word, translation=translation)
        return redirect("word_list")


class EditWordView(View):
    template = "edit_word.html"

    def get(self, request, word_id):
        word = Word.objects.get(id=word_id)
        return render(request, self.template, {"word": word})

    def post(self, request, word_id):
        word = Word.objects.get(id=word_id)
        new_word = request.POST.get("word")
        new_translation = request.POST.get("translation")
        word.word = new_word
        word.translation = new_translation
        word.save()
        return redirect("word_list")
