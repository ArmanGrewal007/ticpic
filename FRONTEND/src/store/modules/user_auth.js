// import EventService from "@/services/event_services";

export const namespaced = true;

export const state = {
    user: null
}

export const getters = {
    // !! is used to convert the value to a boolean
    loggedIn (state) { return !!state.user },
    ifAdmin  (state) { return !!(state.user && state.user.roles.includes('Admin')) }
}