from django.urls import path

from app.serializers.annualoffs import AnnualOffSerializer

from .views import (
    user, employee, geco, transaction, change,
    anomaly, db, sync, overtime,
    annualoffs, payroll, remember, excuse
)

urlpatterns = [
    path('user/profile', user.Profile.as_view()),
    path('user/dashboard', user.Dashboard.as_view()),
    path('defs/employee', employee.EmployeeView.as_view()),
    path('defs/employee/<int:pk>', employee.EmployeeEdit.as_view()),
    path('defs/geco/groups', geco.GecoGroupView.as_view()),
    path('defs/geco/defs', geco.GecoDefView.as_view()),
    path('defs/api/defs', geco.APIDefs.as_view()),
    path('defs/api/groups', geco.APIGroups.as_view()),

    path('ops/transactions', transaction.TransactionView.as_view()),
    # path('ops/create/transactions', transaction.CreateTransactionView.as_view()),
    path('ops/anomalies', anomaly.AnomalyView.as_view()),
    path('ops/check_transaction', change.CheckTransaction.as_view()),
    path('ops/check_anomaly', change.CheckAnomaly.as_view()),
    path('ops/changes', change.ChangeView.as_view()),
    path('ops/overtime', overtime.OvertimeView.as_view()),
    path('ops/annualoffs', annualoffs.AnnualOffView.as_view()),
    path('ops/payroll', payroll.PayrollView.as_view()),

    path('defs/dbs', annualoffs.DBView.as_view()),

    path('integration/changes/waiting_for_approve', change.ForApprove.as_view()),
    path('integration/changes/waiting_for_send', change.ForSend.as_view()),
    path('integration/changes/edit/<int:pk>', change.ChangeEditView.as_view()),
    path('integration/changes/edit/bulk', change.ChangeBulkEditView.as_view()),
    path('integration/changes/send/<int:pk>', change.ChangeSendView.as_view()),
    path('integration/changes/send/bulk', change.ChangeBulkSendView.as_view()),
    path('integration/db', db.DBView.as_view()),
    path('integration/db/edit/<int:pk>', db.DBEdit.as_view()),
    path('integration/sync', sync.Sync.as_view()),
    path('reset/<str:step>/', remember.RememberView.as_view()),
    path('excuse', excuse.ExcuseView.as_view(), name='excuse'),
    path('excuse/<pk>', excuse.ExcuseDetailView.as_view(), name='excuse-detail'),
    path('excuse_send/', excuse.ExcuseApproveSend.as_view(), name='excuse-send'),
    path('excuse_all/approve', excuse.ExcuseAllAproveView.as_view(), name='excuse-all'),
    path('excuses_delete/all', excuse.ExcuseAllDeleteView.as_view(), name='excuse-delete'),
]
