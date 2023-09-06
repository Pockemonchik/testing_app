import { createRouter, createWebHistory } from 'vue-router'
import AuthForm from './components/AuthForm'
import RegistrationForm from './components/RegistrationForm'
import TestingPage from './components/TestingPage'

export default createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/testing', component: TestingPage, alias: '/' },
        { path: '/auth', component: AuthForm },
        { path: '/registration', component: RegistrationForm }
    ]
})