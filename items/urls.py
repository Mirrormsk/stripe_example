from django.urls import path
from items.apps import ItemsConfig
from items.views import ItemDetailView, ItemBuyView, ItemListView

app_name = ItemsConfig.name

urlpatterns = [
    path('', ItemListView.as_view(), name='item-list'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path('buy/<int:pk>/', ItemBuyView.as_view(), name='item_buy'),
]
