import { createStore } from "vuex";
import * as user_auth from "@/store/modules/user_auth.js";


const store = createStore({
    modules:{
        user_auth
    },
    state: {},
    getters: {},
    mutations: {},
    actions: {},
});


export default store