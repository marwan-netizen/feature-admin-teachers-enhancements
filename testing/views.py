"""
Interface layer (Views) for the Testing module.

Handles the user interface for taking tests, submitting answers,
and viewing results.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Test, Result
from accounts.models import Student
from .services import TestingService
import logging

logger = logging.getLogger(__name__)

testing_service = TestingService()

def get_student_id(request):
    """
    Helper to get the student profile ID for the current authenticated user.

    Args:
        request: HTTP request object.

    Returns:
        int or None: Student ID if found, otherwise None.
    """
    if not request.user.is_authenticated: return None
    student = Student.objects.filter(user=request.user).first()
    return student.student_id if student else None

def test_instructions(request):
    """
    Renders the test instructions page.
    """
    return render(request, 'testing/instructions.html')

def start_ai(request):
    """
    Initiates a new AI-powered test session.

    Redirects to the first skill (Reading) after setting up the session.
    """
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    # Seed some session data even if generation fails so the flow can continue with static tests
    if not testing_service.start_dynamic_test_session(request.session):
        request.session['dynamic_tests_ready'] = False
        reading = Test.objects.filter(skill='reading').first()
        listening = Test.objects.filter(skill='listening').first()
        writing = Test.objects.filter(skill='writing').first()
        speaking = Test.objects.filter(skill='speaking').first()

        request.session['dynamic_test_ids'] = {
            'reading': reading.test_id if reading else None,
            'listening': listening.test_id if listening else None,
            'writing': writing.test_id if writing else None,
            'speaking': speaking.test_id if speaking else None,
        }
        request.session.modified = True

    return redirect('testing:reading_start')

# Reading
def reading_start(request):
    """
    Entry point for the Reading portion of the test.
    """
    return redirect('testing:reading_q1')

def reading_q1(request):
    """
    Renders the reading passage and its associated questions.
    """
    test_id = request.session.get('dynamic_test_ids', {}).get('reading')
    if not test_id:
        test = Test.objects.filter(skill='reading').first()
    else:
        test = get_object_or_404(Test, test_id=test_id)

    if test:
        questions = test.questions.prefetch_related('options').all()
        return render(request, 'testing/reading_q1.html', {'test': test, 'questions': questions})
    return render(request, 'testing/reading_q1.html')

def submit_reading(request, q):
    """
    Handles submission of reading test answers.
    """
    student_id = get_student_id(request)
    if not student_id: return redirect('accounts:login')

    if request.method == 'POST':
        test_id = request.session.get('dynamic_test_ids', {}).get('reading')
        if not test_id:
            test = Test.objects.filter(skill='reading').first()
            if not test: return redirect('testing:reading_done')
            test_id = test.test_id

        testing_service.process_mcq_submission(request.user, test_id, student_id, request.POST, 'reading')
        return redirect('testing:reading_done')
    return redirect('testing:reading_done')

def reading_done(request):
    """
    Renders the completion page for the reading section.
    """
    return render(request, 'testing/reading_done.html')

# Listening
def listening_start(request):
    """
    Renders the listening test interface.
    """
    test_id = request.session.get('dynamic_test_ids', {}).get('listening')
    if not test_id:
        test = Test.objects.filter(skill='listening').first()
    else:
        test = get_object_or_404(Test, test_id=test_id)

    if test:
        questions = test.questions.prefetch_related('options').all()
        return render(request, 'testing/listening_q1.html', {'test': test, 'questions': questions})
    return render(request, 'testing/listening_q1.html')

def submit_listening(request, q):
    """
    Handles submission of listening test answers.
    """
    student_id = get_student_id(request)
    if not student_id: return redirect('accounts:login')

    if request.method == 'POST':
        test_id = request.session.get('dynamic_test_ids', {}).get('listening')
        if not test_id:
            test = Test.objects.filter(skill='listening').first()
            if not test: return redirect('testing:listening_done')
            test_id = test.test_id

        testing_service.process_mcq_submission(request.user, test_id, student_id, request.POST, 'listening')
        return redirect('testing:listening_done')
    return redirect('testing:listening_done')

def listening_done(request):
    """
    Renders the completion page for the listening section.
    """
    return render(request, 'testing/listening_done.html')

# Writing
def writing_start(request):
    """
    Renders the writing test topic and input area.
    """
    test_id = request.session.get('dynamic_test_ids', {}).get('writing')
    if not test_id:
        test = Test.objects.filter(skill='writing').first()
    else:
        test = get_object_or_404(Test, test_id=test_id)

    if test:
        return render(request, 'testing/writing_q1.html', {'test': test})
    return render(request, 'testing/writing_q1.html')

def submit_writing(request):
    """
    Handles submission and AI evaluation of the writing test.
    """
    student_id = get_student_id(request)
    if not student_id: return redirect('accounts:login')

    if request.method == 'POST':
        essay = request.POST.get('essay')
        test_id = request.session.get('dynamic_test_ids', {}).get('writing')
        if not test_id:
            test = Test.objects.filter(skill='writing').first()
            if not test: return redirect('testing:writing_done')
            test_id = test.test_id

        if essay:
            testing_service.process_writing_submission(request.user, test_id, student_id, essay)
        return redirect('testing:writing_done')

    return redirect('testing:writing_done')

def writing_done(request):
    """
    Renders the completion page for the writing section.
    """
    return render(request, 'testing/writing_done.html')

# Speaking
def speaking_start(request):
    """
    Renders the speaking test passage for the student to read.
    """
    test_id = request.session.get('dynamic_test_ids', {}).get('speaking')
    if not test_id:
        test = Test.objects.filter(skill='speaking').first()
    else:
        test = get_object_or_404(Test, test_id=test_id)

    if test:
        return render(request, 'testing/speaking_q1.html', {'test': test})
    return render(request, 'testing/speaking_q1.html')

def submit_speaking(request):
    """
    Handles submission of the speaking test transcription and accuracy score.
    """
    student_id = get_student_id(request)
    if not student_id: return redirect('accounts:login')

    if request.method == 'POST':
        transcription = request.POST.get('transcription', '')
        accuracy = int(request.POST.get('accuracy', 0))
        test_id = request.session.get('dynamic_test_ids', {}).get('speaking')

        if not test_id:
            test = Test.objects.filter(skill='speaking').first()
            if not test: return redirect('testing:speaking_done')
            test_id = test.test_id

        testing_service.process_speaking_submission(request.user, test_id, student_id, transcription, accuracy)
        return redirect('testing:speaking_done')
    return redirect('testing:results')

def speaking_done(request):
    """
    Renders the completion page for the speaking section.
    """
    return render(request, 'testing/speaking_done.html')

# Results
def results(request):
    """
    Displays the consolidated results for all tests taken by the user.
    """
    results = Result.objects.filter(user=request.user).select_related('test')
    return render(request, 'testing/results.html', {'results': results})
