from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

try:
    from urllib.parse import quote_plus  # python 3
except:
    pass
from django.db.models import DateTimeField, ExpressionWrapper, F
from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from .models import Post, Theme, Unit, Help, HelpImage, Word, Tag, WordTheme, TagTheme
from .forms import PostForm, ChoiceForm
from django.views import generic
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.utils import timezone
from django.db.models import Q, F, Max, Min, Sum, Count, Case, When, IntegerField
from quiz_app.models import Task, TagTask, Choice, UserTask
from django.db.models.aggregates import Max
from django.forms.models import model_to_dict
from itertools import chain
import time
from datetime import datetime, date, time, timedelta


def blog_create(request):
    if not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)


def blog_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    unit_list = Unit.objects.filter(type__id=instance.id)
    main_list = Post.objects.all()
    context = {
        "title": instance.title,
        "instance": instance,
        "object_list": unit_list,
        "main_list": main_list,
    }
    return render(request, "post_detail.html", context)


def unit_detail(request, slug=None):
    instance = get_object_or_404(Unit, slug=slug)
    # previous_page = Post.objects.filter(id=instance.id)
    theme_list = Theme.objects.filter(inner_unit__id=instance.id)
    main_list = Unit.objects.filter(type__id=instance.type_id)
    main_units = Post.objects.all()
    help_object = Help.objects.filter(inner_unit__id=instance.id)
    # main_list = Unit.objects.all()
    context = {
        "title": instance.title,
        "instance": instance,
        "object_list": theme_list,
        "main_list": main_list,
        "main_units": main_units,
        "help_object": help_object,
    }
    return render(request, "unit_detail.html", context)


def theme_detail(request, slug=None):
    instance = get_object_or_404(Theme, slug=slug)
    progress_percent = 0
    if request.user.is_staff:
        tasks = Task.objects.filter(
            tagtask__tag__id=instance.id,
            usertask__user=request.user).annotate(
            percent=(
                F('usertask__count_true') / F('usertask__count_all'))
        ).values_list(
            'percent', flat=True
        )
        percent = list(tasks)
        if percent == None:
            percent = [0]
        if percent == [None]:
            percent = [0]
        ca = len(percent)
        c_m_05 = 0
        c_l_05 = 0
        for i in range(ca):
            if percent[i] >= 0.5:
                c_m_05 += 1
            else:
                c_l_05 += 1
        ca = Task.objects.filter(
            tagtask__tag__id=instance.id)
        ca = len(ca)
        # progress_percent = 0
        if (ca == 0):
            progress_percent = 0
        else:
            progress_percent = round(((c_m_05 / ca) + (c_l_05 / (2 * ca))) * 100, 1)

    help_object = Help.objects.filter(theme__id=instance.id)
    previous = Unit.objects.filter(type__id=instance.unit_id)
    main = Post.objects.all()
    theme_list = Theme.objects.filter(inner_unit_id=instance.inner_unit_id)

    context = {
        "title": instance.theme_title,
        "instance": instance,
        "help_object": help_object,
        "previous": previous,
        "main": main,
        "theme_list": theme_list,
        "total_progress": progress_percent,
    }
    return render(request, "theme_detail.html", context)


def theme_help(request, slug=None):
    instance = get_object_or_404(Help, slug=slug)
    previous = Theme.objects.get(id=instance.theme_id)
    main = Post.objects.all()
    images = HelpImage.objects.filter(help__id=instance.id)
    context = {
        "title": instance.title,
        "instance": instance,
        "previous": previous,
        "main": main,
        "images": images,
    }
    return render(request, "theme_help.html", context)


def unit_help(request, slug=None):
    instance = get_object_or_404(Help, slug=slug)
    previous = Unit.objects.get(id=instance.inner_unit_id)
    main = Post.objects.all()
    images = HelpImage.objects.filter(help__id=instance.id)
    context = {
        "title": instance.title,
        "instance": instance,
        "previous": previous,
        "main": main,
        "images": images,
    }
    return render(request, "unit_help.html", context)


def profile(request):
    theme_titles = Theme.objects.filter(
        tagtask__task__usertask__user=request.user).annotate(
        t=models.Count('theme_title'))
    theme_ids = Theme.objects.filter(
        tagtask__task__usertask__user=request.user).annotate(
        t=models.Count('theme_title')).values_list('id', flat=True)
    t_ids = list(theme_ids)
    # progress_percent_all = []

    # to_table=Theme.objects.filter(
    #     tagtask__task__usertask__user=request.user).annotate(
    #     t=models.Count('theme_title')).values('theme_title')
    # to_table['themes']={}
    # to_table['pr_all'] = {}
    to_table = []
    to_dict = {}
    for t in t_ids:
        # to_dict.update({'theme':t})
        # to_dict.update({'theme': t})
        # to_table.append(to_dict)
        # to_dict={}
        tasks = Task.objects.filter(
            tagtask__tag__id=t,
            usertask__user=request.user).annotate(
            percent=(
                F('usertask__count_true') / F('usertask__count_all'))
        ).values_list(
            'percent', flat=True
        )
        percent = list(tasks)
        if percent == None:
            percent = [0]
        if percent == [None]:
            percent = [0]
        ca = len(percent)
        c_m_05 = 0
        c_l_05 = 0
        for i in range(ca):
            if percent[i] >= 0.5:
                c_m_05 += 1
            else:
                c_l_05 += 1
        ca = Task.objects.filter(tagtask__tag__id=t)
        ca = len(ca)
        # progress_percent_all = []
        if (ca == 0):
            progress_percent_all = 0
            progress_good = 0
        else:
            progress_percent_all = round(((c_m_05 / ca) + (c_l_05 / (2 * ca))) * 100, 1)
            progress_good = round((c_m_05 / ca) * 100, 1)

        theme = Theme.objects.get(id=t)
        to_dict.update({'theme': theme.theme_title})
        to_dict.update({'pr_all': progress_percent_all})
        to_dict.update({'pr_good': progress_good})
        to_table.append(to_dict)
        to_dict = {}

    theme_ids = progress_percent_all

    context = {
        "theme_titles": theme_titles,
        "progress_percent_all": progress_percent_all,
        "to_table": to_table,
    }
    return render(request, "profile.html", context)


def result(request):
    return render(request, "result.html")


def lookup(request, slug=None):
    instance = get_object_or_404(Theme, slug=slug)
    instance1 = Word.objects.all()

    word_list = Word.objects.filter(wordtheme__theme__id=instance.id)
    previous = Unit.objects.filter(type__id=instance.unit_id)
    previous_unique = instance
    main = Post.objects.all()
    theme_list = Theme.objects.filter(inner_unit_id=instance.inner_unit_id)
    paginator = Paginator(word_list, 1)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
        "title": instance.theme_title,
        "page_request_var": page_request_var,
        "previous": previous,
        "previous_unique": previous_unique,
        "main": main,
        "theme_list": theme_list,
        "instance1": instance1,
    }
    return render(request, "lookup.html", context)


def test(request, slug=None):
    instance = get_object_or_404(Theme, slug=slug)

    # find tasks where percent < 0.5

    tasks = Task.objects.filter(
        tagtask__tag__id=instance.id,
        usertask__user=request.user
    ).annotate(
        percent=(
            F('usertask__count_true') / F('usertask__count_all'))
    ).filter(percent__lt=0.5)
    task = list(chain(tasks))

    # find tasks where percent >= 0.5 and < 0.7

    tasks = Task.objects.filter(
        tagtask__tag__id=instance.id,
        usertask__user=request.user
    ).annotate(
        percent=(
            F('usertask__count_true') / F('usertask__count_all'))
    ).filter(percent__lt=0.7, percent__gte=0.5)
    task = list(chain(task, tasks))

    # find tasks where percent >= 0.7 and < 0.9

    tasks = Task.objects.filter(
        tagtask__tag__id=instance.id,
        usertask__user=request.user
    ).annotate(
        percent=(
            F('usertask__count_true') / F('usertask__count_all'))
    ).filter(percent__lt=0.9, percent__gte=0.7)
    task = list(chain(task, tasks))

    # find tasks where percent >= 0.9 and mun of passed days >= 3

    three_days_ago = timezone.now() - timedelta(days=3)
    tasks = Task.objects.filter(
        tagtask__tag__id=instance.id,
        usertask__user=request.user
    ).annotate(
        percent=(
            F('usertask__count_true') / F('usertask__count_all'))
    ).filter(
        percent__gte=0.9,
        usertask__prev_date__lt=three_days_ago).exclude(
        percent=1
    )
    task = list(chain(task, tasks))

    # find tasks were not seen before

    tasks = Task.objects.filter(
        tagtask__tag__id=instance.id
    ).exclude(usertask__user=request.user)
    task = list(chain(task, tasks))

    # find tasks where percent >= 0.9 and mun of passed days < 3

    three_days_ago = timezone.now() - timedelta(days=3)
    tasks = Task.objects.filter(
        tagtask__tag__id=instance.id,
        usertask__user=request.user
    ).annotate(
        percent=(
            F('usertask__count_true') / F('usertask__count_all'))
    ).filter(percent__gte=0.9, usertask__prev_date__gte=three_days_ago)
    task = list(chain(task, tasks))

    # a = []
    a1 = []
    a2 = []
    a3 = []
    a4 = []
    a5 = []
    a6 = []
    a7 = []
    a8 = []
    a9 = []
    a10 = []
    # a1 = []
    # a2 = []
    # a3 = []
    # a4 = []
    # a5 = []
    # a6 = []
    # a7 = []
    # a8 = []
    # a9 = []
    # a10 = []
    if len(task) >= 10:
        for i in range(0, 10):
            # a.append(Choice.objects.filter(task__id=task[i].id))
            a1 = Choice.objects.filter(task__id=task[0].id)
            a2 = Choice.objects.filter(task__id=task[1].id)
            a3 = Choice.objects.filter(task__id=task[2].id)
            a4 = Choice.objects.filter(task__id=task[3].id)
            a5 = Choice.objects.filter(task__id=task[4].id)
            a6 = Choice.objects.filter(task__id=task[5].id)
            a7 = Choice.objects.filter(task__id=task[6].id)
            a8 = Choice.objects.filter(task__id=task[7].id)
            a9 = Choice.objects.filter(task__id=task[8].id)
            a10 = Choice.objects.filter(task__id=task[9].id)
            # a1 = Choice.objects.filter(task__id=task[0].id)

    ids = []
    if len(task) >= 10:
        ids = [task[0].id, task[1].id, task[2].id, task[3].id, task[4].id, task[5].id, task[6].id, task[7].id,
               task[8].id, task[9].id]
        # task = Task.objects.filter(id__in=ids)

    # answs=[a[0].id, a[1].id, a[2].id, a[3].id, a[4].id, a[5].id, a[6].id, a[7].id, a[8].id, a[9].id]
    # ids = [task[0].id, task[1].id, task[2].id, task[3].id, task[4].id, task[5].id, task[6].id, task[7].id, task[8].id, task[9].id]
    # score=Task.objects.filter(id__in=ids)
    # score=a[1].values_list('id',flat=True)
    answers = Choice.objects.filter(type='yes')
    score = Task.objects.filter(
        tagtask__tag__id=instance.id,
        usertask__user=request.user,
        id__in=ids, choice__in=answers).annotate(
        percent=(
            (F('usertask__count_true') / F('usertask__count_all')) * 100
        ))
    score = len(score)
    # score1 = Choice.objects.filter(type='yes').values('choice_text','task__id')

    # score=round(score[0].percent*100,1)
    if len(task) < 10:
        task = []

    # tags=TagTask.objects.exclude(
    #     tag__id=instance.id).filter(task__in=task).values('tag__theme_title').annotate(t=models.Count("tag")).exclude(tag=None)

    tags = Theme.objects.exclude(
        id=instance.id).filter(tagtask__task__in=task).annotate(t=models.Count('theme_title'))

    # tags=TagTask.objects.all().values('tag').annotate(t=models.Count("tag"))


    # score.user=request.user
    # score.save()

    # question = get_object_or_404(Task, pk=task[0].id)
    # try:
    # selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # except (KeyError, Choice.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(request, 'test.html', {
    #         'question': question,
    #         'error_message': "Ничего не выбрано.",
    #     })
    # else:
    # selected_choice.usertask__count_all += 1
    # selected_uestion = get_object_or_404(Task, pk=task[0].id)
    # try:
    #     selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # except (KeyError, Choice.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(request, 'test.html', {
    #         'question': question,
    #         'error_message': "Ничего не выбрано.",
    #     })
    # else:
    # selected_choice.usertask__count_all += 1
    # selected_choice.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    # return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

    # vote(task_id=task[0].id)
    # question = get_object_or_404(Task, pk=task[0].id)
    # selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # selected_choice.usertask__count_all += 1
    # selected_choice.save()

    # selected_choice = request.POST.get(['choice'], False)
    # selected_choice.usertask__count_all += 1
    # selected_choice.save()


    context = {
        "instance": instance,
        "tasks": score,
        "task": task,
        "a1": a1,
        "tags": tags,
        "a2": a2,
        "a3": a3,
        "a4": a4,
        "a5": a5,
        "a6": a6,
        "a7": a7,
        "a8": a8,
        "a9": a9,
        "a10": a10,

    }
    return render(request, "test.html", context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Ничего не выбрано.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def blog_list(request):
    queryset_list = Post.objects.all()
    query = request.GET.get("query")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query)
            # Q(content__icontains=query)
        ).distinct()
    context = {
        "object_list": queryset_list,
        "title": "List",
    }
    return render(request, "post_list.html", context)


def blog_update(request, slug=None):
    if not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        # instance.user = request.user
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, "post_form.html", context)


def blog_delete(request, slug=None):
    if not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    return redirect("blog:list")
