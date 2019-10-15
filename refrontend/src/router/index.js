import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)

import routes from './routes.js'
const instance =  new Router({
    mode:'history',
    routes
});

export default instance;
