from django.urls import path
from . import views


urlpatterns = [
    path('<int:n1>/<int:n2>', views.task1),

]