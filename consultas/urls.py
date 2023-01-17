from django.urls import path
from . import views
from .views import Record, Login, Logout

app_name = 'consultas'

urlpatterns = [
    path('', views.Consulta, name='Consultas'),
    path('addUser/', Record.as_view(), name="register"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
]