from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from Accounts.models import User, Student, Teacher
from Accounts.forms import userSignUpForm
from django.views.generic import CreateView

# Creating signup for teacher and student
class StudentSignUpView(CreateView):
    model = User
    form_class = userSignUpForm
    template_name = "Accounts/studentSignup.html"

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = "student"

    def form_valid(self, form):
        if form.is_valid():
            user=form.save(commit=False)
            user.is_student=True
            user.save()

class TeacherSignUpView(CreateView):
    model = User
    form_Class = userSignUpForm
    template_name = "Accounts/teacherSignup.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "Teacher"

    def form_valid(self, form):
        if form.is_valid():
            user=form.save(commit=False)
            user.is_teacher=True
            user.save()