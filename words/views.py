from django.shortcuts import render, redirect
from .models import Word, WordGroup
from django.views import View


class WordListView(View):
    template = "word_list.html"

    def get(self, request):
        sort_by = request.GET.get("sort")
        words = Word.objects.all()

        if sort_by == "word":
            words = words.order_by("word")

        return render(request, self.template, {"words": words})


class AddWordView(View):
    template = "add_word.html"

    def get(self, request):
        groups = WordGroup.objects.all()
        return render(request, self.template, {"groups": groups})

    def post(self, request):
        word = request.POST.get("word")
        translation = request.POST.get("translation")
        group_id = request.POST.get("group")

        if group_id:
            group = WordGroup.objects.get(id=group_id)
            Word.objects.create(word=word, translation=translation, group=group)
        else:
            Word.objects.create(word=word, translation=translation)

        groups = WordGroup.objects.all()
        return render(request, self.template, {"groups": groups, "word_added": True})


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


class AddGroupView(View):
    template = "add_group.html"

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        group_name = request.POST.get("group_name")
        WordGroup.objects.create(name=group_name)
        return render(request, self.template, {"group_added": True})
