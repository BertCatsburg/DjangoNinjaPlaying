from ninja import Router

router = Router()

@router.get('/')
def index(request):
    return {"a": "AAA"}

@router.get('/x')
def x_endpoint(request):
    return {"x": "XXX"}
