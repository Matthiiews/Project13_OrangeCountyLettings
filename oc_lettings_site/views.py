from django.shortcuts import render


# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie quam lobortis leo
# consectetur ullamcorper non id est. Praesent dictum, nulla eget feugiat sagittis, sem mi
# convallis eros,
# vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum, eget consequat ipsum
# lobortis quis. Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus. Nullam elementum urna nisi, pellentesque iaculis
# enim cursus in. Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request):
    """
    Render the homepage.

    This view renders the homepage template ('index.html').

    :param HttpRequest request: The HTTP request object.
    :return: Rendered homepage template.
    :rtype: HttpResponse
    """
    return render(request, 'index.html')


def page_not_found(request, exception):
    """
    Handle 404 Page Not Found errors.

    This function renders the custom 404 error page when a requested
    page is not found.

    Args:
        request (HttpRequest): The HttpRequest object representing the client request.
        exception (Exception): The exception object representing the error.

    Returns:
        HttpResponse: The HttpResponse object with a rendered 404 error page and a status code
        of 404.
    """
    response = render(request, "404.html", {})
    response.status_code = 404
    return response


def server_error(request, exception=None):
    """
    Handle 500 Internal Server Error.

    This function renders the custom 500 error page when there is an internal
    server error.

    Args:
        request (HttpRequest): The HttpRequest object representing the client request.
        exception (Exception, optional): The exception object representing the error.
        Defaults to None.

    Returns:
        HttpResponse: The HttpResponse object with a rendered 500 error page and a status code
        of 500.
    """
    response = render(request, "500.html", {})
    response.status_code = 500
    return response
