from django.contrib.postgres.search import SearchVector
from django.db.models import Q

def global_search(query):
    # This would ideally use PostgreSQL Full-Text Search
    # For now, we'll use Q objects to be compatible with SQLite in dev
    from accounts.models import User
    from testing.models import Test
    from classroom.models import Classes

    results = {
        'users': User.objects.filter(Q(email__icontains=query) | Q(full_name__icontains=query)),
        'tests': Test.objects.filter(Q(test_name__icontains=query) | Q(content__icontains=query)),
        'classes': Classes.objects.filter(Q(classes_name__icontains=query) | Q(description__icontains=query))
    }
    return results
