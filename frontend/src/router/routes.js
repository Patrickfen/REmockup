//TODO: use lazy loading: https://alligator.io/vuejs/lazy-loading-vue-cli-3-webpack/
import Home from '@/views/Home.vue'
import Listings from '@/views/Listings.vue'

const routes = [
    {
        path: '/',
        alias: '/home',
        name: 'home',
        component: Home
    },
    {
        path: '/listings',
        name: 'listings',
        component: Listings
    }
]

export default routes;
