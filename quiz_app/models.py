from django.db import models
from django.conf import settings
from blog.models import Theme
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse


# from blog.models import Post

class AppManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(AppManager, self).all()
def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class CommentManager(models.Manager):
    def all(self):
        qs = super(CommentManager, self).all()
        return qs

    def filter_by_instance(self, instance):
        # content_type = ContentType.objects.get_for_model(instance.__class__)
        id = instance.id
        qs = super(CommentManager, self).filter(id=id)
        return qs


class Task(models.Model):
    text = models.CharField(max_length=200)
    image = models.ImageField('Изображение', upload_to=upload_location,
                              null=True,
                              blank=True)
    objects = CommentManager()



    def __str__(self):
        return str(self.text)

    def get_absolute_url(self):
        return reverse("quiz_app:quiz", kwargs={"id": self.id})

    def get_absolute_url_theme(self):
        return reverse("blog:theme", kwargs={"slug": self.slug})

    def get_result_url(self):
        return reverse("quiz_app:result", kwargs={"id": self.id})


class UserTask(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    task = models.ForeignKey(Task, null=True, blank=True, on_delete=models.CASCADE)
    count_all = models.FloatField(default=0)
    count_true = models.FloatField(default=0)
    prev_date = models.DateTimeField('Последний раз пройдено')
    objects = CommentManager()

class TagTask(models.Model):
    tag = models.ForeignKey(Theme, null=True, blank=True, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, null=True, blank=True, on_delete=models.CASCADE)
    objects = CommentManager()

class Choice(models.Model):
    task = models.ForeignKey(Task, null=True, blank=True, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=150)
    type = models.CharField(null=True, blank=True, max_length=3)
    objects = CommentManager()

    def __str__(self):
        return str(self.choice_text)
