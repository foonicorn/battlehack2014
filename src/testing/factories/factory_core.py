import factory

from battlehack.core import models
from testing.factories.factory_user import UserFactory


class CharityFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Charity
    name = factory.Sequence(lambda n: 'Charity #{0}'.format(n))


class ChallengeFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Challenge
    owner = factory.SubFactory(UserFactory)
    title = factory.Sequence(lambda n: 'Challenge #{0}'.format(n))
    description = 'The challenge description'
    charity = factory.SubFactory(CharityFactory)
    amount = 1.50