import { defineStore } from "pinia";

export const useServicesStore = defineStore('services', {
    state: () => ({
        services: [],
        activeServiceIndex: 0,
        activeService: {}
    }),

    getters: {
        getServices: (state) => state.services,
        getEmptyStatus: (state) => state.services.length > 0 ? false : true 
    },

    actions: {
        setStore(data){
            this.services = data?.services

            if (this.services.length > 0){
                this.activeService = this.services[this.activeServiceIndex]
            }
        },

        setActiveService(index){
            this.activeServiceIndex = index
            this.activeService = this.services[this.activeServiceIndex]
        }
    }
})