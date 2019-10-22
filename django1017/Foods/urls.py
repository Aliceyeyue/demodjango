from rest_framework.routers import SimpleRouter
from django1017.views import *
router = SimpleRouter()
router.register(r"API/Food",Foods_View)
