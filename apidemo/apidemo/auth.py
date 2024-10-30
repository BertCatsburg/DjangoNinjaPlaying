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

class APIKeyAuth(APIKeyHeader):
    param_name = "X-API-Key"

    def authenticate(self, request, key):
        if key == "111":
            return key

        return None
