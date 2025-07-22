from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, MyTokenObtainPairSerializer,TodoSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Todo


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=201)
        return Response(serializer.errors, status=400)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class TodoView(APIView):
    
    def get(self,request):
        alldata = Todo.objects.all()
        serializer = TodoSerializer(alldata,many=True)
        return Response("SHOWING FUNCTION IS RUNNING",serializer.data,status=200)
    
    # permission_classes = [isOwnerorReadOnly]

    
    def post(self,request):
        
        alldata=TodoSerializer(data=request.data)
        if alldata.is_valid():
            alldata.save(user=request.user)
            return Response("data saved successfully",alldata.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    def put(self,request):
        
        return Response("update fn run")
    
    def delete(self,request):
        
        return Response("delete fn run")