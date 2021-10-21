from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import *


def survey(request):
    last_question = True
    survey_completed = True
    question = Survey.objects.filter(survey_id='1', user_answer=None)

    if question.count() == 1:
        last_question = True
        question = question[0]

    elif question.count() == 0:
        survey_completed = True

    else:
        question = question[0]
    print(question)
    # if request.method=='POST':
    #     question=request.POST('question')

    params = {'question':question, 'last_question':last_question, 'survey_completed':survey_completed}
    return render(request, 'myadd/customer.html', params)

def save_question(requests):
    if requests.method == 'POST':
        question_id      = requests.POST.get("question_id")
        user_answer      = requests.POST.get("user_answer")
        previous         = requests.POST.get("previous")
        next             = requests.POST.get("next")

        question_obj = Survey.objects.get(pk=question_id)
        question_obj.user_answer = user_answer
        question_obj.user_id = 1
        question_obj.save()
        print(requests.POST)
        return HttpResponseRedirect('/survey')





# def hello(request):
#    return render(request, "hello.html", {})

# def viewArticle(request, articleId):
#    text = "Displaying article Number : %s"%articleId
#    return HttpResponse(text)
#
# def index(request):
#     now = datetime.now()
#
#     return render(
#         request,
#         "HelloDjangoApp/index.html",  # Relative path from the 'templates' folder to the template file
#         # "index.html", # Use this code for VS 2017 15.7 and earlier
#         {
#             'content': "<strong>Hello Django!</strong> on " + now.strftime("%A, %d %B, %Y at %X")
#         }
#     )