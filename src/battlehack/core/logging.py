# -*- coding: utf-8 -*-
from __future__ import absolute_import

import logging
import inspect


def get_logger(obj):
    """Return a logger object with the proper module path for ``obj``."""
    name = None
    module = getattr(inspect.getmodule(obj), '__name__', None)
    if inspect.ismethod(obj):
        name = '{module}.{cls}.{method}'.format(
            module=module,
            cls=obj.im_class.__name__,
            method=obj.__func__.__name__
        )
    elif inspect.isfunction(obj):
        name = '{module}.{function}'.format(
            module=module,
            function=obj.func_name
        )
    elif inspect.isclass(obj):
        name = '{module}.{cls}'.format(
            module=module,
            cls=obj.__name__
        )
    elif isinstance(obj, basestring):
        name = obj

    return logging.getLogger(name)
