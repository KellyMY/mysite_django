import pytest
from django.urls import reverse

@pytest.mark.django_db

def tset_post_view(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status.code == 200
    assert response.content == "Hello World!"