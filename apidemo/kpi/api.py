from ninja import Router

router = Router()

@router.get('/')
def index(request):
    return {"a": "AAA"}

@router.get('/x')
def index(request):
    return {"x": "XXX"}
