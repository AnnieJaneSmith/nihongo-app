from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from unidecode import unidecode

class AppManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(AppManager, self).all()

def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class Post(models.Model):
    title = models.CharField('Заголовок', max_length=120)
    slug = models.SlugField(unique=True)
    image = models.ImageField('Изображение', upload_to=upload_location,
                              null=True,
                              blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    objects = AppManager()

    def save(self):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        super(Post, self).save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:main_unit", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["timestamp"]

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
pre_save.connect(pre_save_post_receiver, sender=Post)

class Unit(models.Model):
    type = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=120)
    slug = models.SlugField(unique=True)
    image = models.ImageField('Изображение', upload_to=upload_location,
                              null=True,
                              blank=True)

    objects = AppManager()

    def save(self):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        super(Unit, self).save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:unit", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-title"]

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

def create_slugU(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Unit.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slugU(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiverU(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slugU(instance)
pre_save.connect(pre_save_post_receiverU, sender=Post)

class Theme(models.Model):
    unit = models.ForeignKey(Post, on_delete=models.CASCADE)
    inner_unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    theme_title = models.CharField('Тема', max_length=350)
    extra_title = models.CharField('Расширенное название', blank=True, null=True, max_length=350)
    image = models.ImageField('Изображение', upload_to=upload_location,
                              null=True,
                              blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.theme_title

    objects = AppManager()

    def save(self):
        if not self.slug:
            self.slug = slugify(unidecode(self.theme_title))
        super(Theme, self).save()

    # def __str__(self):
    #     return self.theme_title

    def get_absolute_url(self):
        return reverse("blog:theme", kwargs={"slug": self.slug})

    def get_view_url(self):
        return reverse("blog:lookup", kwargs={"slug": self.slug})

    def get_test_url(self):
        return reverse("blog:test", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["timestamp"]

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

def create_slugT(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Theme.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slugT(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiverT(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slugT(instance)
pre_save.connect(pre_save_post_receiverT, sender=Theme)

class Help(models.Model):
    # unit = models.ForeignKey(Unit, null=True, blank=True, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, null=True, blank=True, on_delete=models.CASCADE)
    inner_unit = models.ForeignKey(Unit, null=True, blank=True, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    title = models.CharField('Заголовок', max_length=350)
    image = models.ImageField('Изображение', upload_to=upload_location,
                              null=True,
                              blank=True)
    content = models.TextField('Содержание', null=True, blank=True)

    def __str__(self):
        return self.title

    objects = AppManager()

    def save(self):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        super(Help, self).save()

    # def __str__(self):
    #     return self.theme_title

    def get_absolute_url(self):
        return reverse("blog:help", kwargs={"slug": self.slug})

    def get_second_url(self):
        return reverse("blog:helpu", kwargs={"slug": self.slug})

    # class Meta:
    #     ordering = ["timestamp"]

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

def create_slugH(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Help.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slugH(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiverH(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slugH(instance)
pre_save.connect(pre_save_post_receiverH, sender=Help)

class HelpImage(models.Model):
    help = models.ForeignKey(Help, on_delete=models.CASCADE)
    title = models.CharField('Название', null=True, blank=True, max_length=350)
    image = models.ImageField('Изображение', upload_to=upload_location,
                              null=True,
                              blank=True)

    def __str__(self):
        return self.title



class Word(models.Model):
    # theme = models.ForeignKey(Theme, blank=True, null=True, on_delete=models.CASCADE)
    kanji = models.CharField('Слово (кандзи)', blank=True, null=True, max_length=30)
    onyomi = models.CharField('Верхнее чтение', blank=True, null=True, max_length=230)
    kunyomi = models.CharField('Нижнее чтение', max_length=230)
    translation = models.TextField('Перевод', blank=True, null=True, max_length=530)
    def __str__(self):
        return self.kunyomi



class Tag(models.Model):
    title = models.CharField('Название', max_length=350)

    def __str__(self):
        return self.title

class TagTheme(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

# class Task(models.Model):
#     # tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
#     text = models.CharField('Текст задания', max_length=150)
#     ok1 = models.CharField(blank=True, null=True, max_length=3)
#     ok2 = models.CharField(blank=True, null=True, max_length=3)
#     ok3 = models.CharField(blank=True, null=True, max_length=3)
#     ok4 = models.CharField(blank=True, null=True, max_length=3)
#     answer_text1 = models.CharField('Ответ 1', blank=True, null=True,  max_length=150)
#     answer_text2 = models.CharField('Ответ 2', blank=True, null=True,  max_length=150)
#     answer_text3 = models.CharField('Ответ 3', blank=True, null=True,  max_length=150)
#     answer_text4 = models.CharField('Ответ 4', blank=True, null=True,  max_length=150)
#     num1 = models.IntegerField('Количество ответов', blank=True, null=True,  default=0)
#     num2 = models.IntegerField('Количество ответов', blank=True, null=True,  default=0)
#     num3 = models.IntegerField('Количество ответов', blank=True, null=True,  default=0)
#     num4 = models.IntegerField('Количество ответов', blank=True, null=True,  default=0)
#     def __str__(self):
#         return self.text
#
# class TaskTag(models.Model):
#      = models.ForeignKey(Word, blank=True, null=True, on_delete=models.CASCADE)
#     task = models.ForeignKey(Task, on_delete=models.CASCADE)
#
# class TaskTheme(models.Model):
#     theme = models.ForeignKey(Theme, blank=True, null=True, on_delete=models.CASCADE)
#     task = models.ForeignKey(Task, on_delete=models.CASCADE)
#
#
class WordTheme(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
#
#     # def word_of_theme(self, Word):
#     #     if self.word == Word.kunyomi:
#     #         return Word.kunyomi
#
# # class Type(models.Model):
# #     title = models.CharField('Название', max_length=350)
# #     def __str__(self):
# #         return self.title
#
# class Answer(models.Model):
#     task = models.ForeignKey(Task, on_delete=models.CASCADE)
#     ok = models.CharField(blank=True, null=True, max_length=3)
#     answer_text = models.CharField('Текс вопроса', max_length=150)
#     num = models.IntegerField('Количество ответов', default=0)
#     def __str__(self):
#         return self.answer_text




