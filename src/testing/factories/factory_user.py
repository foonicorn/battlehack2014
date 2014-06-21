import factory

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from social.apps.django_app.default.models import UserSocialAuth


class UserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = User
    username = factory.Sequence(lambda i: 'user-{0}'.format(i))
    email = factory.Sequence(lambda i: '{0}@none.none'.format(i))
    first_name = 'foo'
    last_name = 'bar'

    @classmethod
    def _prepare(cls, create, **kwargs):
        raw_password = kwargs.pop('raw_password', 'secret')
        if not 'password' in kwargs:
            kwargs['password'] = make_password(raw_password, hasher='md5')
        return super(UserFactory, cls)._prepare(create, **kwargs)


class SuperUserFactory(UserFactory):
    is_staff = True
    is_superuser = True


class UserSocialAuthFactory(factory.DjangoModelFactory):
    FACTORY_FOR = UserSocialAuth
    user = factory.SubFactory(UserFactory)
    provider = u'github'
    uid = factory.Sequence(lambda i: u'social-{0}'.format(i))
