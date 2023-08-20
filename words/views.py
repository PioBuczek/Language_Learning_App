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
        return render(request, self.template)

    def post(self, request):
        word = request.POST.get("word")
        translation = request.POST.get("translation")
        Word.objects.create(word=word, translation=translation)
        return render(request, self.template)


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


class EditWordListView(View):
    template = "edit_word_list.html"

    def get(self, request):
        words = Word.objects.all()
        return render(request, self.template, {"words": words})


class DeleteWord(View):
    def post(self, request, word_id):
        word = Word.objects.get(id=word_id)
        word.delete()
        return redirect("word_list")
