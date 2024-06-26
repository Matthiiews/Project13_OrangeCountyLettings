from django.test import TestCase
from lettings.models import Address, Letting


class LettingsModelsTestCase(TestCase):

    def test_address_model(self):
        address = Address.objects.create(
            number=100, street="My street", city="My city", state="My state",
            zip_code=10000, country_iso_code="USA")
        excepted_value = "100 My street"
        assert str(address) == excepted_value

    def test_letting_model(self):
        address = Address.objects.create(
            number=100, street="My street", city="My city", state="My state",
            zip_code=10000, country_iso_code="USA")
        letting = Letting.objects.create(title="My letting", address=address)
        excepted_value = "My letting"
        assert str(letting) == excepted_value
