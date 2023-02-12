from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .models import FormInput, Score

def score(request):
    if request.method == 'POST':
        user = request.user
        score = request.POST.get('score', 0)
        
        Score.objects.create(
            user=user,
            score=score,
        )
        
        return redirect('home')
    
    return render(request, 'Qbin/index.html')


def form_submit(request):
    if request.method == 'POST':
        user = request.user
        input_value = request.POST.get('biodegradable')
        
        FormInput.objects.create(
            user=user,
            input_value=input_value,
        )
        
        count = FormInput.objects.filter(user=user).count()
        
        if count >= 10: # 10 is the maximum number of submissions
            Score.objects.create(
                user=user,
                reward_value=100, # 100 is the reward value
            )
        
        return redirect('home')
    
    return render(request, 'Qbin/index.html')


def high_scores(request):
    scores = Score.objects.all().order_by('-score')[:10]
    return render(request, 'Qbin/index.html', {'scores': scores})