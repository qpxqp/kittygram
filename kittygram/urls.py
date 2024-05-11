from django.urls import include, path
from rest_framework.routers import SimpleRouter, DefaultRouter

from cats.views import cat_list, cat_list_detail  # НА ФУНКЦИЯХ
from cats.views import APICat, APICatDetail       # НА КЛАССАХ (низкоуровневые)
from cats.views import CatList, CatDetail         # НА КЛАССАХ (высокоуровневые, Generic)
from cats.views import CatViewSet                 # НА КЛАССАХ (высокоуровневые, ModelViewSet)

# router = SimpleRouter()
router = DefaultRouter()
router.register('api/v1/cats', CatViewSet)

urlpatterns = [
    # НА ФУНКЦИЯХ
    # path('api/v1/cats/', cat_list),
    # path('api/v1/cats/<int:cat_id>/', cat_list_detail),

    # НА КЛАССАХ (низкоуровневые)
    # path('api/v1/cats/', APICat.as_view()),
    # path('api/v1/cats/<int:cat_id>/', APICatDetail.as_view()),

    # НА КЛАССАХ (высокоуровневые, Generic)
    # path('api/v1/cats/', CatList.as_view()),
    # path('api/v1/cats/<int:pk>/', CatDetail.as_view()),

    # НА КЛАССАХ (высокоуровневые, ModelViewSet)
    path('', include(router.urls)),
]
