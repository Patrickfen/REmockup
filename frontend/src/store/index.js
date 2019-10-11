 /* eslint-disable */
import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)


import sessionModule from './sessionModule.js'
export default new Vuex.Store({
    modules:{
        'session':sessionModule
    }
})
