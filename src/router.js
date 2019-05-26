import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/login'
import Registro from '@/components/registro'
import Main from '@/components/Main'
import Codes from '@/components/Codes'
import UsedCodes from '@/components/UsedCodes'
import ScanCode from '@/components/ScanCode'


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
        },
        {
            path: '/home',
            name: 'Home',
            component: Main
        },
        {
            path: '/codes',
            name: 'AvailableCodes',
            component: Codes
        },
        {
            path: '/codes/used',
            name: 'UsedCodes',
            component: UsedCodes
        },
        {
            path: '/scan',
            name: 'ScanCode',
            component: ScanCode
        }
    ]
})
