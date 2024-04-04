import os
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView

from .forms import TextToConvertForm


# Create your views here.


def test(reqest):
    return HttpResponse("działam")

class TestFormView(FormView):
    form_class = TextToConvertForm
    template_name = 'form.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            with open('AI_text_converter/text_from_form.py', 'wt') as file_to_convert:
                file_to_convert.write(form.cleaned_data['text'])
                file_to_convert.close()
            return HttpResponse(f"Data submitted successfully: {form.cleaned_data['text']}")
        else:
            return render(request, self.template_name, {'form': form})