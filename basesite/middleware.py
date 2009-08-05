from basesite.Request_log.models import Request_log

class Request_log_middleware(object):
    def process_request(self, request):
        if request.user.is_anonymous():
            user = None
        else:
            user = request.user
        request_log = Request_log.objects.create(request_url=request.path,
                                                 ipaddress=request.META['REMOTE_ADDR'],
                                                 user=user)
