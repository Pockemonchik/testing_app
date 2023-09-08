import { createRouter, createWebHistory } from 'vue-router'
import AuthForm from './components/AuthForm'
import RegistrationForm from './components/RegistrationForm'
import TestingPage from './components/TestingPage'

const ifAuthenticated = (to, from, next) => {
    if (localStorage.getItem('token')) {
      next();
      return;
    }
    router.push({ 
        path: 'auth'
    });
   };

export const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/testing', component: TestingPage, alias: '/',beforeEnter: ifAuthenticated, },
        { path: '/auth', component: AuthForm },
        { path: '/registration', component: RegistrationForm }
    ]
})



export default router