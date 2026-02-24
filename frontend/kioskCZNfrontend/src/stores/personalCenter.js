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
        getPCName: (state) => state.pcName,
        getEmptyStatus: (state) => {
            if (state.pcId){
                return false
            }else{
                return true
            }
        }
    },

    actions: {
        setStore(data){
            this.urlParam = data?.url_path
            this.pcId = data?.id
            this.pcName = data?.name
        }
    }
})