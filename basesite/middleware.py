'''Custom middlewares'''

from basesite.Request_log.models import RequestLog


class RequestLogMiddleware(object):
    '''Middleware write log of requests '''

    def process_request(self, request):
        '''create RequestLog instance for each request '''

        if request.user.is_anonymous():
            user = None
        else:
            user = request.user
        RequestLog.objects.create(request_url=request.path,
                                  ipaddress=request.META['REMOTE_ADDR'],
                                  user=user)
