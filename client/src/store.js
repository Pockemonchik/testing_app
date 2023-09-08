import { authAPI, testingAPI } from "@/api"
import { createStore } from "vuex"

const store = createStore({
    state: () => ({
        user: {},
        tests: [],
        currentTest: {},
        currentQuestion: {},
        testResult: {
            "questions": []
        },
        testStats: {},
    }),
    mutations: {
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
        setTestStats(state, stats) {
            state.testStats = stats
        },
        appendAnswersToTestResult(state, answers) {
            state.testResult.questions.push({
                "id": this.state.currentQuestion.id,
                "answers": answers
            })
        }
    },
    actions: {
        async login({ commit }, value) {
            const response = await authAPI.auth(value)
            console.log("user in store", response.data)
            if (response.data.token) {
                localStorage.setItem('token', response.data.token);
                console.log("set token", localStorage.getItem('token'))
                commit('setUser', response.data)
            }
        },

        async registration({ commit }, value) {
            const response = await authAPI.registration(value)
            console.log("user in store", response.data)
            if (response.data.token) {
                localStorage.setItem('token', response.data.token);
                console.log("set token", localStorage.getItem('token'))
                commit('setUser', response.data)
            }
        },

        logout({ commit }) {
            localStorage.removeItem('token');
            console.log("logout", localStorage.getItem('token'))
            commit('setUser', {})
        },
        async getTestList({ commit }) {
            const response = await testingAPI.getTestList()
            console.log("getTestList in store", response.data)
            if (response.data) {
                commit('setTests', response.data)
            }
        },
        async getTest({ commit }, id) {
            const response = await testingAPI.getTest(id)
            console.log("getTest in store", response.data)
            if (response.data) {
                commit('setTestResult', {
                    "questions": []
                })
                commit('setCurrentTest', response.data)
                commit('setCurrentQuestion', response.data.questions[0])
            }
            console.log("state", this.state)
        },
        nextQuestion({ commit }, answers) {

            let nextIndex = this.state.currentTest.questions
                .findIndex(q => q.id == this.state.currentQuestion.id) + 1

            if (nextIndex < this.state.currentTest.questions.length) {
                commit('appendAnswersToTestResult', answers)
                console.log("add answers", answers)
                console.log("all answers", this.state.testResult.questions)
                commit('setCurrentQuestion', this.state.currentTest.questions[nextIndex])
            }
            else if (nextIndex == this.state.currentTest.questions.length) {
                    commit('appendAnswersToTestResult', answers)
            }
            else {
                console.log("end of test")
                console.log("TestResult", this.state.testResult)
            }
        },
        async getTestResult({ commit }) {
            const response = await testingAPI.getTestResult(this.state.testResult)
            console.log("getTestResult in store", response.data)
            if (response.data) {
                commit('setTestStats', response.data)
            }
        },
    },
    getters: {
        getUser: s => s.user,
        getCurrentQuestion: s => s.currentQuestion,
        getCurrentQuestionIndex: s => s.currentTest.questions
            ? s.currentTest.questions.findIndex(q => q.id == s.currentQuestion.id) + 1 
            : "",
        getCurrentTestLength: s => s.currentTest.questions 
            ? s.currentTest.questions.length : "",
        getTestStats: s => s.testStats
    }

})

export default store;
