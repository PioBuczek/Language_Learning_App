from django.shortcuts import render, redirect
from .models import Word, WordGroup
from django.views import View


class WordListView(View):
    template = "word_list.html"

    def get(self, request):
        sort_by = request.GET.get("sort")
        category_id = request.GET.get("category")

        words = Word.objects.all()

        if sort_by == "word":
            words = words.order_by("word")

        if category_id:
            words = words.filter(group_id=category_id)

        groups = WordGroup.objects.all()

        return render(request, self.template, {"words": words, "groups": groups})


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


class QuizView(View):
    template = "quiz.html"

    def get(self, request):
        groups = WordGroup.objects.all()

        if not groups:
            return redirect("add_group")

        return render(request, self.template, {"groups": groups})


class QuizStartView(View):
    template = "quiz_start.html"

    def post(self, request):
        group_id = request.POST.get("group")
        selected_group = WordGroup.objects.get(id=group_id)
        words_in_group = Word.objects.filter(group=selected_group)

        if not words_in_group:
            return render(
                request,
                self.template,
                {
                    "selected_group": selected_group,
                    "words_in_group": False,
                },
            )
        elif words_in_group:
            return render(
                request,
                self.template,
                {
                    "selected_group": selected_group,
                    "words_in_group": words_in_group,
                },
            )
        else:
            return render(
                request,
                self.template,
                {
                    "selected_group": selected_group,
                    "words_in_group": False,
                },
            )


class QuizCheckView(View):
    template = "quiz_check.html"

    def post(self, request):
        group_id = int(request.POST.get("group"))
        word_index = int(request.POST.get("word_index"))
        user_translation = request.POST.get("user_translation")
        correct_answers = int(request.POST.get("correct_answers"))

        selected_group = WordGroup.objects.get(id=group_id)
        words_in_group = Word.objects.filter(group=selected_group)

        if word_index < len(words_in_group):
            current_word = words_in_group[word_index]
            correct_translation = current_word.translation.lower()

            is_correct = user_translation.lower() == correct_translation
            if is_correct:
                correct_answers += 1

            next_word_index = word_index + 1
            next_word = (
                words_in_group[next_word_index]
                if next_word_index < len(words_in_group)
                else None
            )

            return render(
                request,
                self.template,
                {
                    "is_correct": is_correct,
                    "correct_translation": correct_translation,
                    "group_id": group_id,
                    "next_index": next_word_index,
                    "updated_correct_answers": correct_answers,
                    "next_word": next_word,
                    "total_words": len(words_in_group),
                },
            )
        else:
            return render(
                request,
                self.template,
                {
                    "quiz_completed": True,
                    "total_words": len(words_in_group),
                    "correct_answers": correct_answers,
                },
            )
