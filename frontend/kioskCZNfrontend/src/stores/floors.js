import { defineStore } from "pinia";

export const useFloorsStore = defineStore('floors', {
    state: () => ({
        floors: []
    }),

    getters: {
        getFloors: (state) => state.floors
    },

    actions: {
        setStore(data){
            this.floors = data?.floors
        }
    }
})