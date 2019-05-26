import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/login'
import Registro from '@/components/registro'

Vue.use(Router)

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'LogIn',
            component: Login
        },
        {
            path: '/register',
            name: 'Register',
            component: Registro
        }
    ]
})
