//TODO: use lazy loading: https://alligator.io/vuejs/lazy-loading-vue-cli-3-webpack/
import Home from '@/views/Home.vue'
import Session from '@/views/Session.vue'

const routes = [
    {
        path: '/',
        name: 'session',
        component: Session
    },
    {
        path: '/home',
        name: 'home',
        component: Home
    }
]

export default routes;
