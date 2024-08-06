from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, LessonForm
from .models import Lesson


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'lessons/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('add_lesson')
    return render(request, 'lessons/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def add_lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.user = request.user
            lesson.save()
            return redirect('add_lesson')
    else:
        form = LessonForm()
    lessons = Lesson.objects.filter(user=request.user)
    return render(request, 'lessons/add_lesson.html', {'form': form, 'lessons': lessons})

def home(request):
    lessons = Lesson.objects.all()
    return render(request, 'lessons/home.html', {'lessons': lessons})


@login_required
def delete_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id, user=request.user)
    lesson.delete()
    return redirect('add_lesson')

@login_required
def edit_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id, user=request.user)
    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES, instance=lesson)
        if form.is_valid():
            form.save()
            return redirect('add_lesson')
    else:
        form = LessonForm(instance=lesson)
    lessons = Lesson.objects.filter(user=request.user)
    return render(request, 'lessons/add_lesson.html', {'form': form, 'lessons': lessons})
