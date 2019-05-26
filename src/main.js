import Vue from 'vue'
import App from './App.vue'
import VueQrcodeReader from 'vue-qrcode-reader'


import './styles/quasar.styl'
import '@quasar/extras/material-icons/material-icons.css'
import {
  Quasar,
  QLayout,
  QHeader,
  QDrawer,
  QPageContainer,
  QPage,
  QToolbar,
  QToolbarTitle,
  QBtn,
  QIcon,
  QList,
  QItem,
  QItemSection,
  QItemLabel,
  QCard,
  QCardSection,
  QCardActions,
  QForm,
  QInput,
  QTable,
  QTh,
  QTr,
  QTd,
  QDialog,
  ClosePopup,
  QSelect,
  QCheckbox,
  QStepper,
  QStep,
  QStepperNavigation,
  QSeparator,
  QDate,
  QImg,
  Loading
} from 'quasar'

Vue.use(Quasar, {
  config: {},
  components: {
    QLayout,
    QHeader,
    QDrawer,
    QPageContainer,
    QPage,
    QToolbar,
    QToolbarTitle,
    QBtn,
    QIcon,
    QList,
    QItem,
    QItemSection,
    QItemLabel,
    QCard,
    QCardSection,
    QCardActions,
    QForm,
    QInput,
    QTable,
    QTh,
    QTr,
    QTd,
    QDialog,
    ClosePopup,
    QSelect,
    QCheckbox,
    QStepper,
    QStep,
    QStepperNavigation,
    QSeparator,
    QDate,
    QImg
  },
  directives: {
  },
  plugins: {
    Loading
  }
 })

 Vue.use(VueQrcodeReader)

import Api from '@/Api'
Vue.prototype.$http  = Api()

Vue.prototype.$user = {
  id: null,
  email: null,
  name: null,
  age: null,
}
Vue.config.productionTip = false

import router from '@/router'

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
