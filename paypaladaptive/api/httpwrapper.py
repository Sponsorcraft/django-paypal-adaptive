from urllib import request


class UrlResponse(object):

    def __init__(self, data, meta, code):
        self.data = data
        self.meta = meta
        self.code = code


class UrlRequest(object):

    def call(self, url, data=None, headers=None):
        if headers is None:
            headers = {}

        request = request.Request(url, data=data, headers=headers)

        try:
            response = request.urlopen(request)

            self._response = UrlResponse(response.read(), response.info(),
                                         response.getcode())
        except request.URLError as e:
            self._response = UrlResponse(e.reason, {}, None)

        return self

    @property
    def response(self):
        return self._response.data

    @property
    def code(self):
        return self._response.code
