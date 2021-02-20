import asyncio
import aiohttp

async def async_api_request(URL, data, headers, method='GET'):
    async with aiohttp.ClientSession(headers=headers) as session:
        if method == 'POST':
            async with session.post(URL, json=data) as request:
                response = await request.json()
                return response
        elif method == 'GET':
            async with session.get(URL, json=data) as request:
                response = await request.json()
                return response
        elif method == 'PUT':
            async with session.put(URL, json=data) as request:
                response = await request.json()
                return response
        elif method == 'PATCH':
            async with session.put(URL, json=data) as request:
                response = await request.json()
                return response


def run_async_task(task):
    try:
        loop = asyncio.get_event_loop()
        results = loop.run_until_complete(task())
        loop.close()
        return results
    except Exception as e:
        return str(e)



