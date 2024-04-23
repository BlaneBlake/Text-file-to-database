import os
from ast import literal_eval

from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView, View

from .forms import TextToConvertForm

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from openai import OpenAI
from dotenv import load_dotenv
from matplotlib import pyplot
from weasyprint import HTML

from .models import Hours


# Create your views here.


def test(reqest):
    return HttpResponse("działam")


# Uploaded data to covert
class DataUploadFormView(FormView):
    form_class = TextToConvertForm
    template_name = 'form.html'

    def get(self, request, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, **kwargs):
        form = self.form_class(request.POST, request.FILES)  # sprawdzić files uploads
        if form.is_valid():

            # Upload text
            with open('AI_text_converter/text_from_form.txt', 'wt') as file_to_convert:
                file_to_convert.write(form.cleaned_data['text'])
                file_to_convert.close()

            # Upload file
            if form.cleaned_data['file'] is not None:
                uploaded_file = request.FILES["file"]
                if os.path.exists('AI_text_converter/file_from_form.txt'):
                    os.remove('AI_text_converter/file_from_form.txt')
                default_storage.save('AI_text_converter/file_from_form.txt', ContentFile(uploaded_file.read()))

            return HttpResponse('Files successfully uploaded')
        else:
            return render(request, self.template_name, {'form': form})


# Create prompt and convert datafiles
class ConvertView(View):
    def get(self, request, **kwargs):

        # Create prompt
        command = (
            'Znajdź w poniższym tekście daty i godziny. zwróć je w formacie listy list:\n'
            '[["YYYY-MM-DD","start_time HH:MM", "end_time HH:MM", "description-text"] ].'

        )

        file = open('AI_text_converter/text_from_form.txt', 'r')
        command += ''.join(file.readlines())
        command += '\n'
        file.close()

        file = open('AI_text_converter/file_from_form.txt', 'r')
        command += ''.join(file.readlines())  # text komendy do ai podać bez htmla
        file.close()

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
        return render(request, 'database-result.html', {"database": database})


# Generate chart
def generate_chart():

    database = Hours.objects.all()
    dates = []
    start_times = []
    end_times = []

    for element in database:
        dates.append(element.date)
        start_times.append((element.start_time.hour * 60 + element.start_time.minute) / 60)
        end_times.append((element.end_time.hour * 60 + element.end_time.minute) / 60)

# Dane wykresu
    pyplot.bar(dates, start_times, label='Start Time', alpha=0.5, color='blue')
    pyplot.bar(dates, end_times, label='End Time', alpha=0.5, color='red')
# Nazwy osi
    pyplot.xlabel('Date')
    pyplot.ylabel('Time')
# Tytuł wykresu
    pyplot.title('Event Timeline')
# Legenda danych
    pyplot.legend()

# Zapis obrazu na wybranej ścieżce
    chart_path = 'AI_text_converter/static/images/chart.png'
    pyplot.savefig(chart_path)

    return chart_path

# Chart view
class ChartsView(View):
    def get(self, request, **kwargs):

        if os.path.exists('AI_text_converter/static/images/chart.png'):
            os.remove('AI_text_converter/static/images/chart.png')

        chart_path = generate_chart()
        return render(request, 'chart.html', {'chart_path': chart_path})


# Generate & download PDF
class PDFGeneratorView(View):
    def get(self, request, **kwargs):

        chart_path = 'AI_text_converter/static/images/chart.png'
        # chart_view_url = "http://127.0.0.1:8000/converter/charts/"
        from django.template.loader import render_to_string
        chart_view_url = render_to_string('AI_text_converter/static/images/chart.png')
        pdf_path = 'AI_text_converter/static/pdf/chart.pdf'

        if os.path.exists(chart_path):
            HTML(url=chart_view_url).write_pdf(pdf_path)
            if os.path.exists(pdf_path):
                return FileResponse(open(pdf_path, 'rb'), as_attachment=True)
            else:
                return HttpResponse('File not found', status=404)
        else:
            return redirect('charts')