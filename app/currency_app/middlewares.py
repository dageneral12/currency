import time
from currency_app.models import ResponseLog
from currency_app.modelchoices import REQUEST_METHODS as RM

# middleware functions universally apply to all
# views.py funcitons, which process requests

# the main logic is in the __call__ magic method

# you need to register middleware in the settings.py
# file as 'currency_app.middlewares.ResponseTimeMiddleware'

# put it at the bottom of the list, as the order is important
# -  middlewares are executed in the same order as
# they appear in the list


class ResponseTimeMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        start = time.time()
        response = self.get_response(request)
        end = time.time()
        response_time = end - start
        print(f'Response time is: {response_time}') # noqa
        # Code to be executed for each request/response after
        # the view is called.
        method = RM[0][1]
        if request.method == 'POST':
            method = RM[0][1]
        elif request.method == 'GET':
            method = RM[1][1]

        print(f'Request method is {method}') # noqa

        ResponseLog.objects.create(
            path=request.path,
            response_time=(end - start)*1000,
            status_code=response.status_code,
            request_methods=method,
        )
        return response

# ResponseLog.objects.all().values('path').annotate(avg_response_time=Avg('response_time'))  # noqa
