# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserApiSerializer
from django.shortcuts import get_object_or_404

# Create your views here.
from .models import UserAPI

class UserApiView(APIView):
    def get(self, request):
        print(request.data.get('email'))
        queryset = UserAPI.objects.filter(email=request.data.get('email'))
        if queryset:
            if queryset.values('password').first()['password']== request.data.get('password'):
                return Response("you are succesfully logged in")
            else:
                return Response("Password is incorrect")
        else:
            return Response("User is not registered")

    def post(self, request):
        queryset=request.data
        serializers= UserApiSerializer(data=queryset)
        if serializers.is_valid(raise_exception=True):
            save_data= serializers.save()

        # return Response("user saved")
        return Response({"Success":"User '{}' created successfully".format(save_data.name)})


    def put (self, request, pk):
        queryset=get_object_or_404(UserAPI.objects.all(),pk=pk)
        parsed_data= request.data
        serializers= UserApiSerializer(instance=queryset, data= parsed_data, partial=True)
        if serializers.is_valid(raise_exception=True):
            save_data= serializers.save()

        # return Response("user saved")
        return Response({"Success":"User '{}' created successfully".format(save_data.name)})


    def delete(self, request, pk):
        queryset = get_object_or_404(UserAPI.objects.all(), pk=pk)
        queryset.delete()

        return Response({"Success": "User '{}' deleted successfully".format(pk)})

