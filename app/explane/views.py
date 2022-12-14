from django.views.generic import CreateView, TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin
from explane.models import Explane
from django.urls import reverse_lazy
from . import forms

class CreateExplaneView(LoginRequiredMixin, CreateView):
    model = Explane
    form_class = forms.CreateExplaneForm
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        return response


class SuccessMessageView(TemplateView):
    template_name = "explane/success.html"