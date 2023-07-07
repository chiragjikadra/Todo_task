from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import TodoSerializer, TodoShareSerializer, TodoAccessLogSerializer, UserSerializer
from .models import Todo, TodoAccessLog, UserModel


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "registration success"}, status=status.HTTP_201_CREATED)
        return Response({"message": "please provide valid data"}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = UserModel.objects.filter(email=email).first()
        if not email or not password:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        if password == user.password:
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)


class TodoListView(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "todo created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailView(APIView):
    def get(self, request, pk):
        todo = Todo.objects.get(owner=pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            todo = Todo.objects.get(owner=pk)
            print(todo)
        except Todo.DoesNotExist:
            return Response("Todo not found", status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        todo = Todo.objects.get(owner=pk)
        todo.delete()
        return Response({"message": "deleted"}, status=status.HTTP_204_NO_CONTENT)


class TodoShareView(APIView):
    def post(self, request, pk):
        print(pk)
        print(request.data)
        todo = Todo.objects.get(owner=pk)
        serializer = TodoShareSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(todo=todo)
            return Response({"message": "todo shared"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoAccessLogView(APIView):
    def get(self, request, pk):
        todo = Todo.objects.get(owner=pk)
        access_logs = TodoAccessLog.objects.filter(todo=todo)
        serializer = TodoAccessLogSerializer(access_logs, many=True)
        return Response(serializer.data)
