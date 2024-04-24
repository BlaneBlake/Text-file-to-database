from django.contrib.auth.models import User
from django.urls import reverse
import pytest

from AI_text_converter.views import HomePageView


# test homepage
@pytest.mark.django_db
def test_homepage(client):
    # Tworzymy użytkownika (pytest nie ma dostępu do bazy danych)
    user = User.objects.create_user(username='User1', password='12345')
    client.login(username='User1', password='12345')

    response = client.get(reverse('home'))
    assert response.status_code == 200

