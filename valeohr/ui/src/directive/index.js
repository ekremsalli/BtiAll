import  { store } from '../store/index'

export const d_perm_checker = {
    bind: function (el, binding) {
      if (!store.state.account.user || !store.getters['account/logged']) el.style.display = 'none'
      else {
        if (store.getters['account/is_superuser'] || store.getters['account/is_staff']) {            
          if (binding.value.only_super && store.getters['account/is_superuser']) {
            el.style.display = binding.value.dx === undefined ? 'block' : binding.value.dx
          } else if (!binding.value.only_super) {
            el.style.display = binding.value.dx === undefined ? 'block' : binding.value.dx
          } else {
            el.style_display = 'none'
          }          
        } else {
          if (!store.getters['account/perms'] || store.getters['account/perms'].length == 0) el.style.display = 'none'
          else {            
            if (binding.value.px) {
              if (store.getters['account/perms'].includes(binding.value.px)) {
                el.style.display = binding.value.dx ? binding.value.dx : 'block'
              } else el.style.display = 'none'
            }                                    
          }
        }
      }
    }
  }