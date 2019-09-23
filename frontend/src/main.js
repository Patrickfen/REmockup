//Imports
import Vue from 'vue'
import axios from 'axios'
import store from '@/store'
import router from '@/router'

//Setup Vue
Vue.config.productionTip = false

//Setup axios
Vue.prototype.axios = axios.create();

//Import root component
import App from './App.vue'

//Import UI framework
import Element from 'element-ui'
//CSS is imported by CDN
Vue.use(Element)

//Create instance
new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')
