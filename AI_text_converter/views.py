import os
from ast import literal_eval

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView

from .forms import TextToConvertForm

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from openai import OpenAI
from dotenv import load_dotenv

from .models import Hours


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
                'Znajdź w poniższym tekście daty i godziny. zwróć je w formacie listy list:\n'
                '[["YYYY-MM-DD","start_time", "end_time", "description-text"] ].'

            )
# Upload text
            with open('AI_text_converter/text_from_form.txt', 'wt') as file_to_convert:
                file_to_convert.write(form.cleaned_data['text'])
                file_to_convert.close()

            file = open('AI_text_converter/text_from_form.txt', 'r')
            command += ''.join(file.readlines())
            command += '\n'
# Upload file
            if form.cleaned_data['file'] is not None:
                uploaded_file = request.FILES["file"]
                if os.path.exists('AI_text_converter/file_from_form.txt'):
                    os.remove('AI_text_converter/file_from_form.txt')
                default_storage.save('AI_text_converter/file_from_form.txt', ContentFile(uploaded_file.read()))

                file = open('AI_text_converter/file_from_form.txt', 'r')
                command += ''.join(file.readlines())   # text komendy do ai podać bez htmla


# AI
            load_dotenv()
            client = OpenAI()

            result = client.completions.create(
                model='gpt-3.5-turbo-instruct',
                prompt=command,
                max_tokens=1000,
                temperature=0.5
            )


# database
            data = result.choices[0].text
            arr_data = literal_eval(data)

            for element in arr_data:
                print(element)
                database_object = Hours.objects.create(date=element[0], start_time=element[1], end_time=element[2],
                                     description=element[3])

            database = Hours.objects.all()

            return render(request, 'database-result.html', {"database":database})
        else:
            return render(request, self.template_name, {'form': form})
