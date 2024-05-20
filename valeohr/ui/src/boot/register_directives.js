import Vue from 'vue'

import '../utils'

import { d_perm_checker } from '../directive'

export default ({ app }) => {
    Vue.directive('perm-checker', d_perm_checker)
}
