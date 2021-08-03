from django.shortcuts import render
from django.http import HttpResponse
from django.urls import exceptions
from rest_framework import viewsets
from .models import Questions
from .serializer import QuestionSerialzer
import requests
from bs4 import BeautifulSoup
import json


def index(request):
    return HttpResponse("Success")


class QuestionAPI(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerialzer


def display(request):
    try:
        res = requests.get("https://stackoverflow.com/questions")
        soup = BeautifulSoup(res.text, "html.parser")
        question = soup.select(".question-summary")
        for que in question:
            q = que.select_one('.question-hyperlink').getText()
            vote_count = que.select_one('.vote-count-post').getText()
            views = que.select_one('.views').attrs['title']
            tags = [i.getText() for i in (que.select('.post-tag'))]
            questions = Questions()
            questions.question = q
            questions.vote_count = vote_count
            questions.views = views
            questions.tags = tags
            questions.save()
        return HttpResponse("Data fetched from stackoverflow")
    except :
        pass
