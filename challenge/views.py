from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser 
from rest_framework import status

from challenge.models import Challenge
from challenge.serializers import ChallengeSerializer 

@csrf_exempt
def challenge_list(request):
    if request.method == 'GET':
        challenge = Challenge.objects.all()
        challenge_serializer = ChallengeSerializer(challenge, many=True)
        return JsonResponse(challenge_serializer.data, safe=False)

    elif request.method == 'POST':
            challenge_data = JSONParser().parse(request)    
            challenge_serializer = ChallengeSerializer(data=challenge_data)
            if challenge_serializer.is_valid():
                challenge_serializer.save() 
                return JsonResponse(challenge_serializer.data, status=status.HTTP_201_CREATED) 
            return JsonResponse(challenge_serializer.errors, status=status.HTTP_422_BAD_REQUEST)

@csrf_exempt 
def challenge_detail(request, pk):
    try: 
        challenge = Challenge.objects.get(pk=pk) 
    except Challenge.DoesNotExist: 
        return HttpResponse(status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        challenge_serializer = ChallengeSerializer(challenge) 
        return JsonResponse(challenge_serializer.data) 
             