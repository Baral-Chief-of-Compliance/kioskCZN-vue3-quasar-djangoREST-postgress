import { defineStore } from "pinia";

export const useDocuments = defineStore('documents',{
    state: () => ({
        documents: [],
        activeDocumentIndex: 0
    }),

    getters: {
        //Получить документы их стора
        getDocuments: (state) => state.documents,

        /**
         * Получить активный документ
         * @param {object} state 
         * @returns {string}
         */
        getDocumentFromActiveDocument(state){
            if (state.documents.length > 0){
                return state.documents[state.activeDocumentIndex].file
            }else{
                return null
            }
        },

        getActiveDocumentName(state){
            if (state.documents.length > 0){
                return state.documents[state.activeDocumentIndex].name
            }else{
                return 'Наименование активного документа'
            }
        }

    },

    actions: {
        /**
         * Установка харанилища документов кадрвого центра
         * @param {array} data 
         */
        setStore(data){
            this.documents = data
        },

        /**
         * Выбрать index активного документа из представаленных 
         * @param {number} index 
         */
        setActiveDocument(index){
            if (this.documents.length >0){
                if (index < this.documents.length){
                    this.activeDocumentIndex = index
                }
            }
        }
    }
})