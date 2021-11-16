from django.shortcuts import render, get_object_or_404
#from .models import Customer, Rider

def d_order_cus(request):
    return render(request, 'orderrequest/order_cus.html')

def d_rider_list(request):
    return render(request, 'orderrequest/rider_list.html')


#### 예제
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)