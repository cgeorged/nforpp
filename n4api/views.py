from django.shortcuts import render
import os
import requests
from django.http import JsonResponse
from .bart import BARTParaphraser

paraphraser = BARTParaphraser()

def paraphrase_text(request):
    if request.method == 'POST':
        input_text = request.POST.get('text')
        if input_text:
            paraphrased_text = paraphraser.paraphrase(input_text)
            return JsonResponse({'paraphrased_text': paraphrased_text})
    return JsonResponse({'error': 'Invalid request'}, status=400)



def parapage(request):
    return render(request, 'paraphrase_form.html', context={})
