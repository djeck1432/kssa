from django.shortcuts import render
from django.views.generic.edit import FormView

from .admin import UserCreationForm


class RegisterFormView(FormView):
    form_class = UserCreationForm
    template_name = "registration.html"
    success_url = "login"

    def form_valid(self, form):
        form.save()

        return super(RegisterFormView, self).form_valid(form)
