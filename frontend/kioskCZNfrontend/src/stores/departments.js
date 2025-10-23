import { defineStore } from "pinia";

export const useDepartments = defineStore('departments', {
    state: () => ({
        departments: []
    }),

    getters: {
        getDepartments: (state) => state.departments
    },

    actions: {
        setStore(data){
            this.departments = data?.departments
        }
    }
})