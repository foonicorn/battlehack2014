from battlehack.core.forms import ChallengeCreateForm
from battlehack.core.models import Challenge
from testing.factories.factory_core import CharityFactory
from testing.factories.factory_user import UserFactory


def test_save_form(db):
    user = UserFactory.create()
    charity = CharityFactory.create()
    data = {
        'title': 'foo',
        'description': 'bar',
        'charity': charity.id,
        'amount': '1.50',
    }
    form = ChallengeCreateForm(data)
    obj = form.save(user)
    challenge = Challenge.objects.get(id=obj.id)
    assert challenge.owner == user
