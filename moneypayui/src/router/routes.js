
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/main/Dashboard.vue'), name: 'dashboard' },
      { path: 'activity', component: () => import('src/pages/main/Activity.vue'), name: 'activity' },
      { path: 'flow', component: () => import('src/pages/main/Flow.vue'), name: 'flow' },
      { path: 'operation', component: () => import('src/pages/main/Operation.vue'), name: 'operation' },
      { path: 'transfer', component: () => import('src/pages/main/Transfer.vue'), name: 'transfer' },
      
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
      }
    ]
  },
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
