from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Model for managing user profiles in the application.

    Represents user profiles in the application, associated with corresponding :class:`User` model
    instances.

    Methods:
        - __str__(): Returns a string representation of the :class:`profile.Profile`.

    Usage:
        The :class:`profile.Profile` model can be used to store additional information about users
        beyond what is provided by the built-in :class:`User` model.

    Example:
        To create a new user profile:
            user = User.objects.create(username='example_user', ...)
            profile = Profile.objects.create(user=user, favorite_city='New York')

    :param user: A one-to-one relationship with the :class:`User` model, linking each profile to a
    :class:`User` account.
    :type user: OneToOneField to :class:`User`
    :param favorite_city: A field for storing the user's favorite city.
    :type favorite_city: CharField, optional
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Return a string representation of the instance.

        This method returns the username of the related user.

        Returns:
            str: The username of the user associated with this instance.
        """
        return self.user.username
