import pytest


@pytest.mark.django_db
def test_user_creation(user_factory):
    user = user_factory(email='test@example.com', password='testpass123')
    assert user.email == 'test@example.com'
    assert user.check_password('testpass123')
