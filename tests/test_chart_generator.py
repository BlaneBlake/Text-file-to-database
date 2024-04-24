import os
from django.urls import reverse
import pytest

@pytest.mark.django_db
def test_chart_generate(client):

    response = client.get(reverse('charts'))

    assert response.status_code == 200

    chart_path = 'AI_text_converter/static/images/chart.png'
    assert os.path.exists(chart_path)
