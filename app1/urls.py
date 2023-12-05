from django.urls import path
from.import views
urlpatterns = [
    path('shows/new',views.method ),
    path('route',views.method1),
    path('show',views.method2),
    path('shows',views.method3),
    path('shows/<int:id>/destroy',views.method4),
    path('shows/<int:num>',views.method5),
    path('route1/<int:num2>',views.method6),
    path('shows/<int:num1>/edit',views.method7 ),

   
]