from django.contrib.sessions.backends.base import UpdateError
from django.core.exceptions import SuspiciousOperation
from token_store import TokenStore

def token_middleware(get_response):
    def middleware(request):
        # process request
        token = request.META.get('HTTP_ACCESS_TOKEN')
        token_session = TokenStore(token)
        # 自动为request添加token_session
        request.token_session = token_session

        response = get_response(request)

        # process response
        try:
            accessed = token_session.accessed
            modified = token_session.modified
            empty = token_session.is_empty()
        except AttributeError:
            pass
        else:
            if accessed:
                if modified and not empty:
                    if response.status_code != 500:
                        try:
                            request.token_session.save()
                        except UpdateError:
                            raise SuspiciousOperation(
                                "The request's token session was deleted before the "
                                "request completed. The user may have logged "
                                "out in a concurrent request, for example."
                            )
        return response

    return middleware
