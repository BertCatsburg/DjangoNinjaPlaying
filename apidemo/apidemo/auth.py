from ninja.security import APIKeyHeader


apikeys = [
    {
        "name": "WUR",
        "key": "09orfj0er9fjo4fjeroijgf094v5rjoedijfgife0t8gj308etghuft8gh05ergidhf085rgrhordjghfe0"
    },
    {
        "name": "Bert",
        "key": "abc123"
    }
]

apikeys2 = [
    {
        "name": "Piet",
        "key": "abc"
    }
]


class APIKeyAuth(APIKeyHeader):
    param_name = "X-API-Key"

    def authenticate(self, request, key):

        foundkey = list(filter(lambda x: x['key'] == key, apikeys))
        print(f"foundkey = {foundkey}")

        if len(foundkey) == 0:
            # Then we have NOT found a matching key
            return None

        print(f'This is customer {foundkey[0]["name"]}')
        return foundkey


class APIKeyAuth2(APIKeyHeader):
    param_name = "X-API-Key2"

    def authenticate(self, request, key):

        foundkey = list(filter(lambda x: x['key'] == key, apikeys2))
        print(f"foundkey = {foundkey}")

        if len(foundkey) == 0:
            # Then we have NOT found a matching key
            return None

        print(f'This is customer {foundkey[0]["name"]}')
        return foundkey
