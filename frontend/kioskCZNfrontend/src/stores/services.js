import { defineStore } from "pinia";

export const useServicesStore = defineStore('services', {
    state: () => ({
        services: [],
        activeServiceIndex: 0,
        activeService: {},
        activeServiceWorkers: []
    }),

    getters: {
        getServices: (state) => state.services,
        getEmptyStatus: (state) => state.services.length > 0 ? false : true 
    },

    actions: {
        /**
         * Установить хранилище услугу кадрового центра
         * @param {object} data 
         */
        setStore(data){
            this.services = data

            if (this.services.length > 0){
                this.activeService = this.services[this.activeServiceIndex]
            }
        },

        /**
         * Установить активную услугу
         * @param {number} index 
         */
        setActiveService(index){
            this.activeServiceIndex = index
            this.activeService = this.services[this.activeServiceIndex]
        },

        /**
         * Установить работников, которые предоставляют активную услугу
         * @param {array} workers 
         */
        setActiveServiceWorkers(workers){
            this.activeServiceWorkers = workers
        }
    }
})