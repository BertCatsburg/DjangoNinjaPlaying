from ninja import NinjaAPI  #, Redoc
from kpi.api import router as kpi_router
from .auth import APIKeyAuth
from ninja.throttling import AnonRateThrottle, AuthRateThrottle


api = NinjaAPI(
    csrf=True,
    throttle=[
        AnonRateThrottle('10/s'),
        AuthRateThrottle('100/s'),
    ],
    # docs=Redoc(),
)

api.add_router("/kpi/", kpi_router, auth=APIKeyAuth())
