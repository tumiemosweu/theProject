from django.shortcuts import get_object_or_404 , render
from django.http import HttpResponse
from django.template import loader

from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ','.join([q.question_text for q in latest_question_list])
    #template = loader.get_template('interview/index.html')
    context = {
            'latest_question_list': latest_question_list,
        }
    return render(request, 'interview/index.html',context)
    #return HttpResponse(output)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'interview/detail.html', {'question': question})
    
    #return HttpResponse("You're looking at question %s." % question_id)