"""Topic 1: Updating entries in Django with UpdateView

This file is a playground for experimenting with Django's UpdateView.
"""

# Minimal example skeleton (not a full Django project)
from django.views.generic import UpdateView
from django.urls import reverse_lazy

# Example model import (replace with your actual model)
# from .models import MyModel


class MyModelUpdateView(UpdateView):
    """Basic UpdateView example for updating an existing object."""

    # model = MyModel          # uncomment and set your model
    # fields = ["field1", "field2"]
    template_name = "mymodel_form.html"
    success_url = reverse_lazy("mymodel_list")

    # You can override methods like form_valid() here to customize behavior.
    # def form_valid(self, form):
    #     return super().form_valid(form)
