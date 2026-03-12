from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import authenticate, login, logout
from accounts.models import User, Student, Teacher
from .serializers import UserSerializer, StudentProfileSerializer, TeacherProfileSerializer
from vocabulary.models import Word, Lesson, Bookmark
from vocabulary.serializers import WordSerializer, LessonSerializer, BookmarkSerializer
from drf_spectacular.utils import extend_schema

class AuthViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    @extend_schema(responses={200: UserSerializer})
    @action(detail=False, methods=['post'])
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    @extend_schema(responses={201: UserSerializer})
    @action(detail=False, methods=['post'])
    def register(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        full_name = request.data.get('full_name')
        role = request.data.get('role', 'student')

        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(email=email, full_name=full_name, password=password, role=role)
        if role == 'student':
            Student.objects.create(user=user)
        elif role == 'teacher':
            Teacher.objects.create(user=user)

        login(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def logout(self, request):
        logout(request)
        return Response({'status': 'logged out'})

    @extend_schema(responses={200: UserSerializer})
    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(user_id=self.request.user.user_id)

    serializer_class = UserSerializer

    @extend_schema(responses={200: StudentProfileSerializer})
    @action(detail=False, methods=['get'])
    def student(self, request):
        try:
            profile = request.user.student_profile
            serializer = StudentProfileSerializer(profile)
            return Response(serializer.data)
        except Student.DoesNotExist:
            return Response({'error': 'Not a student'}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(responses={200: TeacherProfileSerializer})
    @action(detail=False, methods=['get'])
    def teacher(self, request):
        try:
            profile = request.user.teacher_profile
            serializer = TeacherProfileSerializer(profile)
            return Response(serializer.data)
        except Teacher.DoesNotExist:
            return Response({'error': 'Not a teacher'}, status=status.HTTP_404_NOT_FOUND)

class VocabularyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('q')
        if query:
            return Word.objects.filter(word__icontains=query)
        return super().get_queryset()

class LessonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookmarkViewSet(viewsets.ModelViewSet):
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ActivityViewSet(viewsets.ModelViewSet):
    from analytics.models import UserActivity
    from analytics.serializers import ActivitySerializer
    queryset = UserActivity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role == 'admin':
            return self.queryset
        return self.queryset.filter(user=self.request.user)
