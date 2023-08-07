from django.shortcuts import render, redirect
from .models import Word


def word_list(request):
    words = Word.objects.all()
    return render(request, "word_list.html", {"words": words})


def add_word(request):
    if request.method == "POST":
        word = request.POST.get("word")
        translation = request.POST.get("translation")
        Word.objects.create(word=word, translation=translation)
        return redirect("word_list")
    else:
        message = "Wprowadz słowko i translacje."
        return render(request, "add_word.html", {"message": message})
