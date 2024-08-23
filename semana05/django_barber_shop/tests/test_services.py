import pytest
from rest_framework.test import APIClient
from rest_framework import status


@pytest.fixture
def client_with_token():
    client = APIClient()

    role_data = {
        'name': 'ADMIN'
    }
    role = client.post('/api/v1/authentication/role/create/', role_data, format='json')
    assert role.status_code == status.HTTP_201_CREATED

    user_data = {
        'name': 'Eduardo',
        'email': 'eduardo@gmail.com',
        'password': '123456',
        'phone': '987654321',
        'role_id': role.data['data']['id']
    }
    user = client.post('/api/v1/authentication/user/create/', user_data, format='json')
    assert user.status_code == status.HTTP_201_CREATED

    credentials = {
        'email': user_data['email'],
        'password': user_data['password'],
    }
    response = client.post('/api/v1/authentication/login/', credentials, format='json')
    assert response.status_code == status.HTTP_200_OK
    
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {response.data['access']}')

    return client

@pytest.mark.django_db
def test_services_create(client_with_token):
    data = {
        'name': 'Corte de Pelo',
        'description': 'Descripcion corte de pelo',
        'price': 50,
        'duration': 1
    }
    response = client_with_token.post('/api/v1/services/create/', data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['message'] == 'Service created successfully'
    assert isinstance(response.data['data'], dict)
    assert response.data['data']['name'] == data['name']
    assert response.data['data']['description'] == data['description']


@pytest.mark.django_db
def test_services_list(client_with_token):
    response = client_with_token.get('/api/v1/services/list/')

    assert response.status_code == status.HTTP_200_OK
    assert response.data['message'] == 'Services fetched successfully'
    assert isinstance(response.data['data'], list)