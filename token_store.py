from django.core.cache import caches
from django.conf import settings
from django.contrib.sessions.backends.cache import SessionStore


class TokenStore(SessionStore):
    """Cache-based token store system.

    It used like http sessions.
    """

    def __init__(self,
                 token=None,
                 namespace=None,
                 cache_alias=settings.SESSION_CACHE_ALIAS):

        self._cache = caches[cache_alias]
        self._namespace = None
        self.set_namespace(namespace)

        super(SessionStore, self).__init__(token)

    @property
    def cache_key_prefix(self):
        return f'token_{self.namespace}_' if self.namespace else 'token_'

    @property
    def namespace(self):
        return self._namespace

    def set_namespace(self, namespace):
        if namespace is not None:
            assert isinstance(namespace, str)
        self._namespace = namespace

    @property
    def token(self):
        return self.session_key

    def create_token(self):
        self.create()
        self.modified = False
