from django.core.urlresolvers import reverse

from battlehack.core import views
from testing.factories.factory_request import RequestFactory
from testing.factories.factory_user import UserFactory


def test_index_view(rf):
    url = reverse('core:index')
    assert url
    request = rf.get(url)
    response = views.index(request)
    assert response.status_code == 200


def test_logout_view(db):
    url = reverse('core:logout')
    assert url
    user = UserFactory.create()
    request = RequestFactory.get(url, user=user)
    assert request.user.is_authenticated()
    response = views.logout(request)
    assert response.status_code == 200
    assert not request.user.is_authenticated()
