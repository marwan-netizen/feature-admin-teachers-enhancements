from rest_framework import viewsets, permissions
from .models import Classes, OnlineSession, Assignment, AssignmentSubmission, Grade
from .serializers import ClassSerializer, OnlineSessionSerializer, AssignmentSerializer, SubmissionSerializer, GradeSerializer

class ClassroomViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ClassSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role == 'teacher':
            return Classes.objects.filter(teacher__user=self.request.user)
        return Classes.objects.filter(classstudent__student__user=self.request.user)

class SessionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OnlineSessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return OnlineSession.objects.filter(class_info__classstudent__student__user=self.request.user)

class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role == 'teacher':
            return Assignment.objects.filter(teacher__user=self.request.user)
        return Assignment.objects.filter(class_info__classstudent__student__user=self.request.user)

class GradeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = GradeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Grade.objects.filter(user=self.request.user)
