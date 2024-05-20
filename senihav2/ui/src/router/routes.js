
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Dashboard.vue'), name: 'dashboard' },
      { path: 'trendyol/urun_aktarimi', component: () => import('pages/trendyol/CreateProduct.vue'), name: 'trendyol/urun_aktarimi' },
      { path: 'trendyol/urun_esleme', component: () => import('pages/trendyol/ProductMatch.vue'), name: 'trendyol/urun_esleme' },
      { path: 'trendyol/eksik_eslesme', component: () => import('pages/trendyol/Mismatch.vue'), name: 'trendyol/eksik_eslesme' },
      { path: 'trendyol/siparis_gecmisi', component: () => import('pages/trendyol/Log.vue'), name: 'trendyol/siparis_gecmisi' }

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
  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
