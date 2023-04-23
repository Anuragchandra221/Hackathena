from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Questions
from rest_framework.response import Response
from .serializers import *
import random

# Create your views here.
@api_view(['GET'])
def question(request):
    try:
        question = Questions.objects.filter(id=1)
        if(Questions.objects.filter(id=1).count()<1):
            return Response({"msg":"no questions available"}) 
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data) 
    except: 
        return Response({"msg":"no questions available"}) 

@api_view(['POST'])
def next_question(request):
    data = request.data['question']
    answer = request.data['answer']
    question = Questions.objects.get(id=data)
    print(question)
    if(answer==1):
        lower = question.option_one_lower
        upper = question.option_one_upper
    elif(answer==2):
        lower = question.option_two_lower
        upper = question.option_two_upper
    elif(answer==3):
        lower = question.option_three_lower
        upper = question.option_three_upper
    elif(answer==4):
        lower = question.option_four_lower
        upper = question.option_four_upper
    else:
        lower = question.option_five_lower
        upper = question.option_five_upper
    num = random.randint(lower,upper)
    try:
        question = Questions.objects.filter(id=num)
        if(Questions.objects.filter(id=num).count()<1):
            return Response({"msg":"no questions available"}) 
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data) 
    except: 
        return Response({"msg":"no questions available"}) 