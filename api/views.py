from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from .models import Contact
from .serializers import ContactSerializer
# Create your views here.

@api_view(['GET'])
def getContacts(request):
    contact = Contact.objects.all().order_by('first_name')
    serializer = ContactSerializer(contact, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getContact(request, pk):
    contact = Contact.objects.get(id=pk)
    serializer = ContactSerializer(contact, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createContact(request):
    data = request.data
    contact = Contact.objects.create(
        first_name=data['first_name'],
        last_name=data['last_name'],
        phone_number=data['phone_number'],
        gender=data['gender'],
        email=data['email']
    )
    serializer = ContactSerializer(contact, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateContact(request, pk):
    data = request.data
    contact = Contact.objects.get(id=pk)
    serializer = ContactSerializer(instance=contact, data=data)
    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteContact(request, pk):
    contact = Contact.objects.get(id=pk)
    contact.delete()
    return Response('Contact was deleted!')