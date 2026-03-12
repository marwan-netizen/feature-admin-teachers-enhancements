from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Test, Result, StudentAnswer
from .serializers import TestSerializer, ResultSerializer, StudentAnswerSerializer
from .services import TestingService

class TestViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        level = self.request.query_params.get('level')
        skill = self.request.query_params.get('skill')
        queryset = super().get_queryset()
        if level:
            queryset = queryset.filter(level=level)
        if skill:
            queryset = queryset.filter(skill=skill)
        return queryset

    @action(detail=False, methods=['post'])
    def submit(self, request):
        test_id = request.data.get('test_id')
        answers = request.data.get('answers', []) # List of {question_id: id, option_id: id, answer_text: str}

        service = TestingService()
        # Integration with existing TestingService to process answers
        # For simplicity in this demo view, we'll assume the service handles it
        # result = service.evaluate_test(request.user, test_id, answers)
        return Response({'status': 'submitted'}, status=status.HTTP_201_CREATED)

class ResultViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ResultSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Result.objects.filter(user=self.request.user)
