import { defineStore } from "pinia";


export const usePCStore = defineStore('personalCenter', {
    state: () => ({
        urlParam: null,
        pcId: null, 
        pcName: 'Наименование КЦ'
    }),

    getters: {
        getUrlParam: (state) => state.urlParam,
        getPCId: (state) => state.pcId,
        getPCName: (state) => state.pcName
    },

    actions: {
        setStore(data){
            this.urlParam = data?.personnel_center
            this.pcId = data?.object
            this.pcName = data?.pc_name
        }
    }
})