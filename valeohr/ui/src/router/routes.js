
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Dashboard.vue'), name: 'dashboard' },
      { path: 'defs/employee', component: () => import('pages/defs/Employee.vue'), name: 'defs/employee' },
      { path: 'defs/geco/groups', component: () => import('pages/defs/GecoGroup.vue'), name: 'defs/geco/groups' },
      { path: 'defs/geco/defs', component: () => import('pages/defs/GecoDef.vue'), name: 'defs/geco/defs' },

      { path: 'ops/transactions', component: () => import('pages/ops/Transaction.vue'), name: 'ops/transactions' },
      { path: 'ops/anomalies', component: () => import('pages/ops/Anomaly.vue'), name: 'ops/anomalies' },
      { path: 'ops/overtime', component: () => import('pages/ops/Overtime.vue'), name: 'ops/overtime' },
      { path: 'ops/annualoffs', component: () => import('pages/ops/Annualoffs.vue'), name: 'ops/annualoffs' },
      { path: 'ops/payroll', component: () => import('pages/ops/Payroll.vue'), name: 'ops/payroll' },


      { path: 'integration/changes_for_approve', component: () => import('pages/integration/ChangesForApprove.vue'), name: 'integration/changes_for_approve' },
      { path: 'integration/changes_for_send', component: () => import('pages/integration/ChangesForSend.vue'), name: 'integration/changes_for_send' },
      { path: 'integration/sync', component: () => import('pages/integration/Sync.vue'), name: 'integration/sync' },
      { path: 'integration/db', component: () => import('pages/integration/Db.vue'), name: 'integration/db' },


    ]
  },
  {
    path: '/p/',
    component: () => import('layouts/PublicLayout.vue'),
    children: [
      {
        path: 'login',
        component: () => import('pages/account/Login.vue'),
        name: 'login',
        meta: {
          public: true
        }
      },
      {
        path: 'remember',
        component: () => import('pages/account/Remember.vue'),
        name: 'remember',
        meta: {
          public: true
        }
      },    
    ]
  },
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
