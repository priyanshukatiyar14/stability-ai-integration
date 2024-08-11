from django.http import JsonResponse
from celery import group
from stability_ai.tasks import generate_image

def generate_images(request):
    prompts = ["A red flying dog", "A piano ninja", "A footballer kid"]
    task_group = group(generate_image.s(prompt) for prompt in prompts)
    result = task_group.apply_async()
    return JsonResponse({"result": result.id})