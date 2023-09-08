import { authAPI, testingAPI } from "@/api"
import {createStore} from "vuex"

const store = createStore({
    state : () => ({
        user: {},
        tests: [],
        currentTest:{},
        currentQuestion:{},
        testResult:{}

    }),
    mutations :{
        setUser(state, user) {
            state.user = user
        },
        setTests(state, tests) {
            state.tests = tests
        },
        setCurrentTest(state, test) {
            state.currentTest = test
        },
        setCurrentQuestion(state, question) {
            state.currentQuestion = question
        },
        setTestResult(state, result) {
            state.testResult = result
        },
    },
    actions :{
        async auth({ commit }, value) {
            const response = await authAPI.auth(value)
            console.log("user in store",response.data)
            if(response.data.token){
                localStorage.setItem('token', response.data.token);
                console.log("set token",localStorage.getItem('token'))
                commit('setUser', response.data)
            }
        },
        logout({ commit }) {
                localStorage.removeItem('token');
                console.log("logout",localStorage.getItem('token'))
                commit('setUser', {})
        },
        async getTestList({ commit }) {
            const response = await testingAPI.getTestList()
            console.log("getTestList in store",response.data)
            if(response.data){
                commit('setTests', response.data)
            }
        },
        async getTest({ commit },id) {
            const response = await testingAPI.getTest(id)
            console.log("getTest in store",response.data)
            if(response.data){
                commit('setCurrentTest', response.data)
                commit('setCurrentQuestion', response.data.questions[0])
            }
            console.log("state",this.state)
        },
        nextQuestion({ commit }) {
            let nextIndex = this.state.currentTest.questions
                .findIndex(q => q.id == this.state.currentQuestion.id)+1
            
            if (nextIndex<this.state.currentTest.questions.length) {
                commit('setCurrentQuestion',this.state.currentTest.questions[nextIndex])
            }
            else {
                console.log("end of test")
            }
        },  
    },
    getters : {
        getUser: s => s.user,
        getCurrentQuestion: s => s.currentQuestion,
    }

})

export default store;
