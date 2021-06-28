import webargs
import webargs.djangoparser
import functools

from rest_framework.response import Response
from get_price_api import exceptions

def validate_data(schema):
    def decorator(view):
        def view_wrapper(self,request,*args, **kwargs):
            try:
                parsed_data = webargs.djangoparser.parser.parse(schema,request)
                print(parsed_data)
            except webargs.ValidationError as e:
                return Response(status = 400,data = "Invalid data")
            except (exceptions.OfferValException,exceptions.OfferTypeException, exceptions.DistanceValException) as e:
                return Response(status = 400,data = e.message)
            kwargs.update({'data': parsed_data})
            return view(self,request,*args,**kwargs)
        return view_wrapper
    return decorator

validate_post_data = functools.partial(validate_data)
