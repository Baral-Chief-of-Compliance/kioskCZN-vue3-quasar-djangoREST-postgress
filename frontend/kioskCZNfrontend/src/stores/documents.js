import { defineStore } from "pinia";

export const useDocuments = defineStore('documents',{
    state: () => ({
        documents: []
    }),

    getters: {
        getDocuments: (state) => state.documents
    },

    actions: {
        setStore(data){
            this.documents = data?.documents
        }
    }
})