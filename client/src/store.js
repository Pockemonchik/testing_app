import { authAPI } from "@/api"
import {createStore} from "vuex"

const store = createStore({
    state : () => ({
        user: {},

    }),
    mutations :{
        setUser(state, user) {
            state.user = user
        },
    },
    actions :{
        async auth({ commit }, value) {
            const user = await authAPI.auth(value)
            commit('setUser', user)
        },
    },
    getters : {
        user: s => s.user,
    
    }

})

export default store;
