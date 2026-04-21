from django.urls import path, include

urlpatterns = [
    path('api/', include('books.urls')),
    path('api/', include('carts.urls')),
    path('api/', include('orders.urls')),
]
