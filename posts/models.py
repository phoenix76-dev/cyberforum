from django.db import models
from django.contrib.auth.models import User


def empty_user():
    return User.objects.get(username='deleted')


class Thank(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='question_thanks_fk')
    answer = models.ForeignKey('Answer', on_delete=models.CASCADE, related_name='answer_thanks_fk')
    from_user = models.ForeignKey(User, on_delete=empty_user, related_name='from_user_thanks_fk')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user_thanks_fk')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Благодарность'
        verbose_name_plural = 'Благодарности'

    def __str__(self):
        return 'Thanks in question {0} to user {1} for answer {2}'\
            .format(self.question.id, self.to_user.username, self.answer.id)


class SectionBase(models.Model):
    title = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    short_name = models.CharField(max_length=10, default='')
    messages_count = models.BigIntegerField(default=0)
    topics_count = models.BigIntegerField(default=0)
    last_activity = models.ForeignKey('Question', blank=True, null=True, default=None, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=empty_user, related_name='section_author_fk')

    class Meta:
        abstract = True


class Section(SectionBase):
    is_subsections = models.BooleanField(default=False)


class Subsection(SectionBase):
    parent = models.ForeignKey(Section, on_delete=models.SET_NULL, related_name='subsection_author_fk')


class PostBase(models.Model):
    


class Declaration(models.Model):
    title = models.CharField(max_length=200, default='')
    content = models.TextField(default='')
    author = models.ForeignKey(User, on_delete=empty_user)
    views_count = models.BigIntegerField(default=0)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    updater = models.ForeignKey(User, on_delete=empty_user, related_name='updated_declarations_fk')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return 'Объявление {0}'.format(self.title)


class ImportantNote(models.Model):
    title = models.CharField(max_length=200, default='')
    content = models.TextField(default='')
    author = models.ForeignKey(User, on_delete=empty_user)
    views_count = models.BigIntegerField(default=0)
    answers_count = models.IntegerField(default=0)
    is_commentary = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    updater = models.ForeignKey(User, on_delete=empty_user, related_name='updated_notes_fk')

    class Meta:
        verbose_name = 'Важный пост'
        verbose_name_plural = 'Важные посты'

    def __str__(self):
        return 'Важный пост {0}'.format(self.title)


class Question(models.Model):
    title = models.CharField(max_length=200, default='')
    content = models.TextField(default='')
    author = models.ForeignKey(User, on_delete=empty_user)
    best_answer = models.ForeignKey('Answer', blank=True, null=True, default=None, related_name='what_best_answer_fk')
    views_count = models.BigIntegerField(default=0)
    answers_count = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    updater = models.ForeignKey(User, null=True, blank=True, on_delete=empty_user, related_name='updated_questions_fk')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return 'Вопрос {0}'.format(self.title)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers_fk')
    content = models.TextField(default='')
    author = models.ForeignKey(User, on_delete=empty_user)
    index = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    updater = models.ForeignKey(User, null=True, blank=True, on_delete=empty_user, related_name='updated_answers_fk')

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return 'Ответ номер {0} в вопросе {1}'.format(self.index, self.question_id)
