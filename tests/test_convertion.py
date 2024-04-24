from django.urls import reverse
import pytest

from AI_text_converter.models import Hours


@pytest.mark.django_db
def test_convertion(client):

    with open('AI_text_converter/text_from_form.txt', 'w') as text:
        text.write('19-03-2024 07.00-15.00 test')
        text.close()
    with open('AI_text_converter/file_from_form.txt', 'w') as file:
        file.write('19-03-2024 07.00-15.00 test')
        file.close()

    response = client.get(reverse('convert-data'))

    assert response.status_code == 200
    assert Hours.objects.count() > 0