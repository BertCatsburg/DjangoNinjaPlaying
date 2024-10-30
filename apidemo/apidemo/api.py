from ninja import NinjaAPI
from kpi.api import router as kpi_router
from .auth import APIKeyAuth

api = NinjaAPI(csrf=True)

api.add_router("/kpi/", kpi_router, auth=APIKeyAuth())
