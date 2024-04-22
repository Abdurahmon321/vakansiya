from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    path("singup", views.singup, name="singup"),
    path("login", views.user_login, name="login"),
    path("logout", views.logout, name="logout"),

    path("vakansiya_list", views.vakansiya_list, name="vakansiya_list"),
    path("add_vakansiya", views.create_vakansiya, name="add_vakansiya"),
    path("update_vakansiya/<int:id>", views.update_vakansiya, name="update_vakansiya"),
    path("detail_vakansiya/<int:id>", views.vakansiya_detail, name="detail_vakansiya"),
    path('delete_vakansiya/<int:id>/', views.vakansiya_delete, name='delete_vakansiya'),

    path('user_profile/<int:id>/', views.user_profile, name='user_profile'),
    path("user_profile_edit/<int:id>/", views.user_profile_edit, name="user_edit_profile"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

