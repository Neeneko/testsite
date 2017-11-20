# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging ; logger = logging.getLogger("board")
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect


from .forms import LoginForm,LogoutForm,CreateTopicForm,CreateCommentForm
from .models import Author,Topic,Comment

DEFAULT_PAGE    =   'authors.html'

def index(request):
    logger.info("Session Keys : [%s]" % str(request.session.keys()))
    template = loader.get_template('board/index.html')
    context = {}
    if request.session.has_key('author_name'):
        context["author_name"]    =   request.session["author_name"]
        context["current_page"]    =   request.session.get("current_page",DEFAULT_PAGE)
        context["form"]    =   LogoutForm()
    else:
        context["form"]    =   LoginForm()



    return HttpResponse(template.render(context, request))

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            author_name =   form.cleaned_data['author_name']
            if not Author.objects.filter(name=author_name).exists():
                logger.info("No such author")
                author = Author(name=author_name)
                author.save()


            request.session["author_name"]  =   form.cleaned_data['author_name']
            request.session["curernt_page"] =   'board/authors.html'
            return HttpResponseRedirect('/board')

def logout(request):
    del request.session["author_name"]
    template = loader.get_template('board/reload.html')
    return HttpResponse(template.render({'redirect_url':'/board'}, request))
#--------------------------------------------------------------------------------
#   Thread level views
#--------------------------------------------------------------------------------
def threads(request):
    template = loader.get_template('board/threads.html')
    context                 =   {}
    context["thread_list"]  =   Topic.objects.all()
    context["author_name"]  =   request.session["author_name"]
    context["form"]         =   CreateTopicForm()
    return HttpResponse(template.render(context, request))

def delete_thread(request,thread_id):
    current_thread  =   Topic.objects.get(pk=thread_id)
    Comment.objects.filter(thread=current_thread).delete()
    current_thread.delete()
    return threads(request)

def view_thread(request,thread_id):

    current_thread  =   Topic.objects.get(pk=thread_id)
    thread_author   =   current_thread.author
    template        =   loader.get_template('board/thread.html')
    context = {}
    context['title']        =   current_thread.title
    context['desc']         =   current_thread.desc
    context['author']       =   thread_author.name
    context['thread_id']    =   current_thread.pk
    context['form']         =   CreateCommentForm()
    context['comment_list'] =   Comment.objects.filter(thread=current_thread).order_by('-created')
    return HttpResponse(template.render(context, request))

def create_thread(request):
    if request.method == 'POST':
        form = CreateTopicForm(request.POST)
        if form.is_valid():
            thread_title    =   form.cleaned_data['topic_name']
            thread_desc     =   form.cleaned_data['topic_desc']
            current_author  =   Author.objects.get(name=request.session["author_name"])
            topic           =   Topic(title=thread_title,desc=thread_desc,author=current_author)
            topic.save()
            logger.info("Created Topic with ID [%s]" % topic.pk)
            return view_thread(request,topic.pk)

def create_comment(request,thread_id):
    if request.method == 'POST':
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            current_thread  =   Topic.objects.get(pk=thread_id)
            current_author  =   Author.objects.get(name=request.session["author_name"])
            text            =   form.cleaned_data['text']
            comment         =   Comment(text=text,author=current_author,thread=current_thread)
            comment.save()
            logger.info("Created Comment with ID [%s]" % comment.pk)
            return view_thread(request,current_thread.pk)

    return view_thread(request,thread_id)


#--------------------------------------------------------------------------------
#   Author level views
#--------------------------------------------------------------------------------

def authors(request):
    template = loader.get_template('board/authors.html')
    context                 =   {}
    context["author_list"]  =   Author.objects.all()
    logger.info("Author List [%s]" %  Author.objects.all())
    context["author_name"]  =   request.session["author_name"]
    return HttpResponse(template.render(context, request))

def delete_author(request,author_id):
    logger.info("Authro Id [%s]" % author_id)
    current_author  =   Author.objects.get(name=request.session["author_name"])
    target_author   =   Author.objects.get(pk=author_id)
    anonymous       =   Author.objects.get(name='anonymous')
    logger.info("Currnet [%s]" % current_author)
    logger.info("Target [%s]" % target_author)

    Topic.objects.filter(author=target_author).update(author=anonymous)
    Comment.objects.filter(author=target_author).update(author=anonymous)


    isCurrent       =   current_author == target_author
    target_author.delete()
    #TODO - logic to re-reference existing threads

    if isCurrent:
        return logout(request)
    else:
        return authors(request)


