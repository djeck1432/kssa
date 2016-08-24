from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст статьи')
    image = models.ImageField(upload_to='images', verbose_name='Картинка',
                              blank=True, default=None)
    pub_date = models.DateTimeField(verbose_name='Опубликована', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class History(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст статьи')
    image = models.ImageField(upload_to='images', verbose_name='Картинка',
                              blank=True, default=None)
    pub_date = models.DateTimeField(verbose_name='Опубликована', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Статья | История'
        verbose_name_plural = 'Статьи | История'


class Faq(models.Model):
    question = models.CharField(max_length=255, verbose_name='Вопрос')
    answer = models.TextField(verbose_name='Ответ')

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['-id']
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'
