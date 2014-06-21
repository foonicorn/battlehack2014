import factory
from django.contrib.auth import SESSION_KEY, BACKEND_SESSION_KEY
from django.contrib.auth.middleware import get_user
from django.contrib.auth.models import AnonymousUser
from django.contrib.messages.storage.base import BaseStorage
from django.contrib.sessions.backends.signed_cookies import SessionStore
from django.test.client import RequestFactory as DjangoRequestFactory
from django.utils.functional import SimpleLazyObject


class RequestFactory(factory.StubFactory):
    @classmethod
    def get(cls, path=None, **kwargs):
        kwargs['path'] = path
        kwargs['method'] = DjangoRequestFactory().get
        return cls.stub(**kwargs)

    @classmethod
    def post(cls, path=None, **kwargs):
        kwargs['path'] = path
        kwargs['method'] = DjangoRequestFactory().post
        return cls.stub(**kwargs)

    @classmethod
    def stub(cls, **kwargs):
        method = kwargs.pop('method')
        path = kwargs.pop('path', '/test/')
        data = kwargs.pop('data', {})
        session = kwargs.pop('session', SessionStore())
        user = kwargs.pop('user', None)
        auth_backend = kwargs.pop('backend',
            'django.contrib.auth.backends.ModelBackend')
        request = method(path, data, **kwargs)
        request.session = session
        if user:
            request.session[SESSION_KEY] = user.id
            request.session[BACKEND_SESSION_KEY] = auth_backend
            request.user = SimpleLazyObject(lambda: get_user(request))
        else:
            request.user = AnonymousUser()
        request._messages = BaseStorage(request)
        return request
