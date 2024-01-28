# from .views import VehicleViewSet

from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r"book", BookViewSet, basename="book")
router.register(r"borrow_book", BorrowBookViewSet, basename="borrow_book")
