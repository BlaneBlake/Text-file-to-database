import os
from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_pdf_generator_view(client):

    response = client.get(reverse('pdf'))

    assert response.status_code == 200 or response.status_code == 302

    assert os.path.exists('AI_text_converter/static/pdf/chart.pdf')