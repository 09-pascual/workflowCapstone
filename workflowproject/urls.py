from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from workflowapi.views import (
    ProjectViewSet, GroupViewSet, ProjectGroupViewSet,
    InvoiceViewSet, GroupWorkerViewSet, ClientViewSet,
    WorkerViewSet, ProjectWorkerViewSet, TaskViewSet,
    UserViewSet, login_user, register_user
)

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'clients', ClientViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'groupworkers', GroupWorkerViewSet)
router.register(r'invoices', InvoiceViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'projectgroups', ProjectGroupViewSet)
router.register(r'projectworkers', ProjectWorkerViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'users', UserViewSet)
router.register(r'workers', WorkerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-token-auth', obtain_auth_token),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)