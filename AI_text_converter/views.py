import os
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView

from .forms import TextToConvertForm

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

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
        form = self.form_class(request.POST, request.FILES)  # sprawdzić files uploads
        if form.is_valid():

            command = (
                'Znajdź w poniższym tekście daty i godziny. zwróć je w formacie:\n'
                '"date: dd-mm-yyyy, start time: hh:mm, end time: hh:mm, description: description-text". \n'
                )

            with open('AI_text_converter/text_from_form.txt', 'wt') as file_to_convert:
                file_to_convert.write(form.cleaned_data['text'])
                file_to_convert.close()

            file = open('AI_text_converter/text_from_form.txt', 'r')
            command += ''.join(file.readlines())
            command += '\n'

            if form.cleaned_data['file'] is not None:
                uploaded_file = request.FILES["file"]
                if os.path.exists('AI_text_converter/file_from_form.txt'):
                    os.remove('AI_text_converter/file_from_form.txt')
                default_storage.save('AI_text_converter/file_from_form.txt', ContentFile(uploaded_file.read()))

                file = open('AI_text_converter/file_from_form.txt', 'r')
                command += ''.join(file.readlines())   # text komendy do ai podać bez htmla

            print(command)

            return HttpResponse(f"<p>Data submitted successfully!</p>"
                                f"<p>textarea: {form.cleaned_data['text']}</p>"
                                f"<p>file: {form.cleaned_data['file']}</p>"
                                f"<p>{command}</p>")
        else:
            return render(request, self.template_name, {'form': form})
