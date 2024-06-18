from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Profile

import logging

logger = logging.getLogger(__name__)


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed consequat libero
# pulvinar eget. Fusc
# faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum lacus d


def index(request):
    """
    Render the profiles index page.

    This view retrieves all user profiles from the database and renders
    the profiles index page ('profiles_index.html') with a list of user profiles.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered template.
    """
    logger.debug("profiles-DEBUG")
    logger.info("profiles-INFO")
    logger.warning("profiles-WARNING")
    logger.error("profiles-ERROR")
    logger.critical("profiles-CRITICAL")

    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)

# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate. Sed tincidunt, dolor
# id facilisis fringilla, eros leo tristique lacus,
# it. Nam aliquam dignissim congue. Pellentesque habitant morbi tristique senectus et netus et
# males


def profile(request, username):
    """
    Render the details page for a specific user profile.

    This view retrieves a user profile with the specified username from the database
    and renders the details page ('profile.html') with information about the user profile.

    Parameters:
        request (HttpRequest): The HTTP request object.
        username (str): The username of the user profile to display.

    Returns:
        HttpResponse: The HTTP response object containing the rendered template.
    """
    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
