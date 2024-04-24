import os
import pytest
from django.urls import reverse


# test wejścia na stronę
@pytest.mark.django_db
def test_request(client):
    response = client.get(reverse('upload-form'))
    assert response.status_code == 200


# test wysłania danych i zapisu na serwer
@pytest.mark.django_db
def test_valid_data(client):
    data = {
        'text': 'testowy tekst',
        'file': open('tests/test_text_file.txt', 'r')
    }

    response = client.post(reverse('upload-form'), data)

    assert response.status_code == 200
    assert os.path.exists('AI_text_converter/text_from_form.txt')
    assert (os.path.exists('AI_text_converter/file_from_form.txt'))


@pytest.mark.django_db
def test_invalid_data(client):
    data = {
        'text': '',
        'file': ''
    }

    with pytest.raises(ValueError):
        client.post(reverse('upload-form'), data)


