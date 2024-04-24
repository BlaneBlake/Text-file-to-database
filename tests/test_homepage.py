from django.contrib.auth.models import User
from django.urls import reverse
import pytest


# test homepage
@pytest.mark.django_db
def test_homepage_logout(client):

    user = User.objects.create_user(username='User1', password='12345')
    response = client.get(reverse('home'))
    # przekierowanie do logowania jeśli niezalogowany
    assert response.status_code == 302


@pytest.mark.django_db
def test_homepage_login(client):

    user = User.objects.create_user(username='User1', password='12345')
    client.login(username='User1', password='12345')
    response = client.get(reverse('home'))
    # wchodzi na stronę po zalogowaniu
    assert response.status_code == 200
