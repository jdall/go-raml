import json
import aiohttp


class HTTPClient:
    def __init__(self, loop, base_uri="<no value>"):
        self.base_url = base_uri
        self.session = aiohttp.ClientSession(loop=loop)
        self.headers = {"Content-Type": "application/json"}

    def set_auth_header(self, val):
        ''' set authorization header value'''
        self.headers["Authorization"] = val

    def close(self):
        self.session.close()

    def build_header(self, headers):
        hdrs = self.headers
        if headers is None:
            return hdrs

        for key in headers:
            hdrs[key] = headers[key]
        return hdrs

    async def get(self, uri, data, headers, params, content_type):
        res = await self.session.get(uri, data=data, headers=self.build_header(headers), params=params)
        res.raise_for_status()
        return res

    async def delete(self, uri, data, headers, params, content_type):
        res = await self.session.delete(uri, data=data, headers=self.build_header(headers), params=params)
        res.raise_for_status()
        return res

    async def post(self, uri, data, headers, params, content_type):
        hdrs = self.build_header(headers)
        if not isinstance(data, str):
            data = json.dumps(data)

        res = await self.session.post(uri, data=data, headers=hdrs, params=params)
        res.raise_for_status()
        return res

    async def put(self, uri, data, headers, params, content_type):
        hdrs = self.build_header(headers)
        if not isinstance(data, str):
            data = json.dumps(data)

        res = await self.session.put(uri, data=data, headers=hdrs, params=params)
        res.raise_for_status()
        return res

    async def patch(self, uri, data, headers, params, content_type):
        hdrs = self.build_header(headers)
        if not isinstance(data, str):
            data = json.dumps(data)

        res = await self.session.patch(uri, data=data, headers=hdrs, params=params)
        res.raise_for_status()
        return res
