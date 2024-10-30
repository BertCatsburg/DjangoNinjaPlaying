from ninja import NinjaAPI
from kpi.api import router as kpi_router

api = NinjaAPI()

api.add_router("/kpi/", kpi_router)
