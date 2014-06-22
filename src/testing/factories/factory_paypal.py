import factory

from battlehack.paypal import models
from testing.factories.factory_core import ChallengeFactory


class PaymentFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Payment
    challenge = factory.SubFactory(ChallengeFactory)
    pid = factory.Sequence(lambda n: 'PAY-{0}'.format(n))
    type = models.TYPE_OWNER
