from django.conf import settings


def config(request):
    parameters = [
        'DEBUG',
    ]

    context = {}
    for parameter in parameters:
        context[parameter] = getattr(settings, parameter, None)

    return context
