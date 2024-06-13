from django.test import TestCase
from django.urls import reverse, resolve

from lettings.models import Address, Letting


class LettingsUrlsTestCase(TestCase):

    def setUp(self):
        self.address = Address.objects.create(
            number=100, street="My street", city="My city", state="My state", zip_code=10000,
            country_iso_code="USA")
        self.letting = Letting.objects.create(title="My letting", address=self.address)

    def test_letting_index(self):
        path = reverse('lettings:index')
        assert path == "/lettings/"
        assert resolve(path).view_name == "lettings:index"

    def test_letting_url(self):
        letting_id = self.letting.id
        path = reverse('lettings:letting', args=[letting_id])
        # print(path)
        assert path == f"/lettings/{letting_id}/"
        assert resolve(path).view_name == "lettings:letting"
