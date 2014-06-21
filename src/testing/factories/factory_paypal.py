import factory

from battlehack.paypal import models
from testing.factories.factory_core import ChallengeFactory
from testing.factories.factory_user import UserFactory


class PaymentFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Payment
    challenge = factory.SubFactory(ChallengeFactory)
    user = factory.SubFactory(UserFactory)
    pid = factory.Sequence(lambda n: 'PAY-{0}'.format(n))
    type = models.TYPE_OWNER
    status = models.STATUS_CREATED
