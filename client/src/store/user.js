import { authAPI } from "@/api"

export const state = () => ({
    user: {},
})

export const mutations = {
    setUser(state, user) {
        state.user = user
    },

}
 
export const actions = {
    async auth({commit}) {
        const user = await authAPI.auth()
        commit('setUser', user)
    },
    
}

export const getters = {
    user: s => s.user,
    
}