from django.urls import path
from .views import (
    arp, 
    op, 
    user, 
    flow, 
    activity,
    service,
    call
)

urlpatterns = [
    path('arp', arp.ARPView.as_view(), name='arp_view'),
    path('service', service.ServiceView.as_view(), name='service_view'),
    path('call', call.CallView.as_view(), name='call_view'),

    path('user/profile', user.Profile.as_view()),
    path('user/dashboard', user.Dashboard.as_view()),
    path('user/change_password', user.ChangePassword.as_view()),
    path('flow', flow.FlowView.as_view()),
    path('activity', activity.ActivityView.as_view({'get': 'list'})),
    path('op', op.OpView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('op/<int:pk>', op.OpView.as_view({
        'get': 'retrieve',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
    path('op/detail', op.OpDetailView.as_view({
        'get': 'list',
        'post': 'create' 
    })),
    path('op/detail/<int:pk>', op.OpDetailView.as_view({
        'get': 'retrieve',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
]