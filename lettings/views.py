from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Letting

import logging


logger = logging.getLogger(__name__)

# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit. Sed non placerat
# massa. Integer est nunc, pulvinar a
# tempor et, bibendum id arcu. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices
# posuere cubilia curae; Cras eget scelerisque


def index(request):
    """
    Render the lettings index page.

    This view retrieves all letting properties from the database and renders the lettings
    index page ('lettings_index.html') with a list of letting properties.

    :param request: The HTTP request object.
    :type request: HttpRequest

    :return: The HTTP response object containing the rendered template.
    :rtype: HttpResponse
    """
    logger.debug("lettings-DEBUG")
    logger.info("lettings-INFO")
    logger.warning("lettings-WARNING")
    logger.error("lettings-ERROR")
    logger.critical("lettings-CRITICAL")

    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non. In accumsan porta nisl id
# eleifend.
# Praesent dignissim, odio eu consequat pretium, purus urna vulputate arcu, vitae efficitur
#  lacus justo nec purus. Aenean finibus faucibus lectus at porta. Maecenas auctor, est ut luctus
# congue, dui enim mattis enim, ac condimentum velit libero in magna. Suspendisse potenti.
# In tempus a nisi sed laoreet.
# Suspendisse porta dui eget sem accumsan interdum. Ut quis urna pellentesque justo mattis
# ullamcorper ac non tellus. In tristique mauris eu velit fermentum, tempus pharetra est luctus.
# Vivamus consequat aliquam libero, eget bibendum lorem. Sed non dolor risus. Mauris condimentum
# auctor elementum. Donec quis nisi ligula. Integer vehicula tincidunt enim, ac lacinia augue
# pulvinar sit amet.


def letting(request, letting_id):
    """
    Render the details page for a specific letting property.

    This view retrieves a letting property with the specified ID from the database and renders the
    details page ('letting.html') with information about the letting property, including its
    title and address.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :param letting_id: The ID of the letting property to display.
    :type letting_id: int

    :return: The HTTP response object containing the rendered template.
    :rtype: HttpResponse
    """
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
