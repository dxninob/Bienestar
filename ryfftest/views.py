from django.shortcuts import render
from django.http import HttpResponse
from ryfftest.models import Question

# Create your views here.

def ryfftest(request):
  questions = Question.objects.all()
  context = {'questions':questions}
  return render(request, 'ryfftest.html', context)