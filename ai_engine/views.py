"""
Interface layer (Views) for the AI Engine module.

Handles HTTP requests for AI-powered features like streaming explanations
and chatbot interactions.
"""

import json
import logging
import requests
import os
import uuid
import urllib.parse
from django.http import StreamingHttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.db import transaction
from testing.models import Test, Question, Option, StudentAnswer, Result, Evaluation
from .models import ChatSession
from .application.factory import AIServiceFactory

logger = logging.getLogger(__name__)
ai_service = AIServiceFactory.create_standard_service()

def ollama_explain(request):
    """
    Streams an English explanation for a test question using a local Ollama instance.

    Args:
        request: HTTP request object containing 'question', 'correct_answer', and 'student_answer'.

    Returns:
        StreamingHttpResponse: A stream of tokens explaining the mistake.
    """
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        data = json.loads(request.body)
        question = data.get('question')
        correct_answer = data.get('correct_answer')
        student_answer = data.get('student_answer')
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    prompt = f"""You are a helpful English teacher. A student answered a question incorrectly on an English test.

Question: {question}
Student's answer: {student_answer}
Correct answer: {correct_answer}

Explain briefly (3-4 sentences max) why the student's answer is wrong and why the correct answer is right. Be encouraging and clear. Use simple English."""

    def event_stream():
        ollama_url = os.getenv('OLLAMA_URL', 'http://localhost:11434') + '/api/generate'
        payload = {
            'model': os.getenv('OLLAMA_MODEL', 'tinyllama:1.1b'),
            'prompt': prompt,
            'stream': True,
            'options': {
                'temperature': 0.7,
                'num_predict': 256,
            },
        }

        try:
            response = requests.post(ollama_url, json=payload, stream=True, timeout=60)
            for line in response.iter_lines():
                if line:
                    chunk = json.loads(line.decode('utf-8'))
                    if 'response' in chunk:
                        yield f"data: {json.dumps({'token': chunk['response']})}\n\n"
                    if chunk.get('done'):
                        yield "data: [DONE]\n\n"
        except Exception as e:
            logger.error(f'Ollama streaming error: {str(e)}')
            yield f"data: {json.dumps({'token': 'AI explanation is temporarily unavailable.'})}\n\n"
            yield "data: [DONE]\n\n"

    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')

def generate_tests_groq():
    """
    Utility function to trigger comprehensive test generation via Groq.

    Returns:
        ComprehensiveTestDTO: The generated test suite.
    """
    return ai_service.generate_comprehensive_test()

def evaluate_with_gemini(text, skill):
    """
    Utility function to evaluate student input via Gemini.

    Args:
        text: The text to evaluate.
        skill: The skill category.

    Returns:
        dict: Evaluation results.
    """
    return ai_service.evaluate_response(text, skill)

def chatbot_history(request):
    """
    Retrieves the chatbot message history for the authenticated user.

    Args:
        request: HTTP request object.

    Returns:
        JsonResponse: List of previous messages in the session.
    """
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Unauthorized'}, status=401)

    history = ChatSession.objects.filter(user=request.user).order_by('created_at')
    data = [{'role': chat.role, 'content': chat.content} for chat in history]
    return JsonResponse(data, safe=False)

def chatbot_send(request):
    """
    Handles sending a new message to the AI chatbot and getting a response.

    Args:
        request: HTTP request object containing 'message'.

    Returns:
        JsonResponse: The AI's response text.
    """
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Unauthorized'}, status=401)

        message = request.POST.get('message')
        if not message:
            return JsonResponse({'error': 'Message required'}, status=400)

        with transaction.atomic():
            ChatSession.objects.create(user=request.user, role='user', content=message)

            # Use Gemini for real AI response
            eval_res = evaluate_with_gemini(message, 'writing')
            response_text = eval_res.get('feedback', 'I am your English tutor. How can I help today?')

            ChatSession.objects.create(user=request.user, role='model', content=response_text)

        return JsonResponse({'status': 'success', 'response': response_text})
    return JsonResponse({'error': 'Method not allowed'}, status=405)

def strengthening_plan(request):
    """
    Renders the student's personal strengthening plan page.

    Args:
        request: HTTP request object.

    Returns:
        HttpResponse: Rendered HTML page.
    """
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    return render(request, 'core/strengthening.html')

def generate_listening_openrouter():
    """
    Utility function to trigger listening test generation via OpenRouter.

    Returns:
        List[TestDTO]: List of generated listening tests.
    """
    return ai_service.generate_listening_test()
