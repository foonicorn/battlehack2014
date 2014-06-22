import factory

from battlehack.paypal import models
from testing.factories.factory_core import AttendeeFactory


class PaymentFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Payment
    attendee = factory.SubFactory(AttendeeFactory)
    pid = ''
