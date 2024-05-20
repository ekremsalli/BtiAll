from django.urls import path

from app.views import (users, log_error, armon_api, organization, logo_api, truncate)

app_name = 'app'

urlpatterns = [
    path('users', users.UsersView.as_view(), name='users'),
    path('login', users.LoginUserApi.as_view(), name='login'),
    path('users/detail/<int:pk>/', users.UserDetailView.as_view(), name="user-detail"),
    path('role', users.UserRoleView.as_view(), name="user-role"),
    path('role/<pk>', users.UserRolesView.as_view(), name="user-role"),
    path('role/<user_id>/<organization_id>', users.UserRoleDelete.as_view(), name="user-role-delete"),
    path('change-password/<pk>', users.ChangePasswordView.as_view(), name='change-password'),

    path('organization', organization.OrganizationView.as_view(), name="organization"),
    path('organization/list', organization.OrganizationListView.as_view(), name="organization-list"),
    path('organization/sync', organization.OrganizationSyncView.as_view(), name="organization-sync"),

    path('armonapi', armon_api.ArmonApiView.as_view(), name="armon-api"),
    path('logoapi', logo_api.LogoApiView.as_view(), name="logo-api"),
    path('logerrors', log_error.LogoErrorView.as_view(), name="logo-error"),
    path('log/errors/<int:pk>/', log_error.LogErrorDetailView.as_view(), name="logo-error-delete"),
    path('log/errors/<organization_id>', log_error.LogoErrorListView.as_view(), name="logo-error-list"),
    path('logerrors/sendAll/<organization_id>', log_error.LogErrorTotalSend.as_view(), name="logo-error-total-send"),
    path('truncate', truncate.TruncateView.as_view(), name="truncate"),
    path('user/change/password',users.UserChangePasswordView.as_view(),name="user-change-password")
]
