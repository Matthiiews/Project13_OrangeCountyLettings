from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Model for managing physical addresses.

    Represents a physical address with attributes such as number, street, city, state,
    zip code, and country ISO code.

    Methods:
        - __str__: Returns a string representation of the :class:`lettings.Address`.

    :param number: The street number of the :class:`lettings.Address`.
    :type number: PositiveIntegerField, required
    :param street: The name of the street.
    :type street: CharField, required
    :param city: The name of the city.
    :type city: CharField,required
    :param state: The state abbreviation (e.g., 'CA' for California).
    :type state: CharField, required
    :param zip_code: The ZIP code of the :class:`lettings.Address`.
    :type zip_code: PositiveIntegerField, required
    :param country_iso_code: The ISO code of the country (e.g., 'USA' for United States).
    :type country_iso_code: CharField, required
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        """
        Return a string representation of the Address instance.

        This method returns the address as a string in the format:
        "<number> <street>".

        Returns:
            str: A string that combines the address number and street.
        """
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Model for managing letting properties.

    Represents a :class:`lettings.Letting` (rental) property with a title and an associated
    :class:`lettings.Address`.

    Methods:
        - __str__: Returns a string representation of the :class:`lettings.Letting` property.

    :param title: The title or name of the :class:`lettings.Letting` property.
    :type title: CharField, required
    :param address: A one-to-one relationship with an :class:`lettings.Address`.
    :type address: OneToOneField to :class:`lettings.Address`, required
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Return a string representation of the Letting instance.

        This method returns the title of the letting.

        Returns:
            str: The title of the letting.
        """
        return self.title
