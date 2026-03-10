from django.shortcuts import render
from django.views import View
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserActivity
from vocabulary.models import Bookmark

class StudentDashboardView(LoginRequiredMixin, View):
    def get(self, request):
        activities = UserActivity.objects.filter(user=request.user).order_by('-timestamp')[:10]
        bookmarks_count = Bookmark.objects.filter(user=request.user).count()

        activity_stats = UserActivity.objects.filter(user=request.user).values('activity_type').annotate(count=Count('id'))

        return render(request, 'analytics/dashboard.html', {
            'activities': activities,
            'bookmarks_count': bookmarks_count,
            'stats': activity_stats
        })

class TeacherDashboardView(LoginRequiredMixin, View):
    def get(self, request):
        # Only teachers can see this
        if request.user.user_type != 'teacher' and not request.user.is_staff:
            return render(request, '403.html', status=403)

        total_activity = UserActivity.objects.count()
        popular_words = UserActivity.objects.filter(activity_type='dictionary_lookup').values('metadata__word').annotate(count=Count('id')).order_by('-count')[:5]

        return render(request, 'analytics/teacher_dashboard.html', {
            'total_activity': total_activity,
            'popular_words': popular_words
        })
