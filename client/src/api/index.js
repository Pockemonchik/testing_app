import axios from "axios"
import request from "./request"

export const authAPI = {
    async auth(params) {
        console.log("auth start api/", params)
        try {
            let res = await request.post("/auth/", params)
            console.log("auth/", res)
            return res
        }
        catch (e) {
            console.log(e)
        }
    },
    async registration(params) {
        console.log("registration start api/", params)
        let res = await request.post("/registration/", params)
        console.log("registration/", res)
        return res
    }
}


export const testingAPI = {
    async getTestList() { 
        console.log("test list api/")
        let res = await request.get("testing/tests/")
        console.log("test list api  res/", res)
        return res
    },
    async getTest(id) { 
        console.log("test detail api/")
        let res = await request.get(`testing/tests/${id}`)
        console.log("test detail api res/", res)
        return res
    },
    async sendTestResult(params) { 
        console.log("test results api/", params)
        let res = await request.post(`testing/results/`, params)
        console.log("test results api res/", res)
        return res
    },
}
