import { defineStore } from "pinia";

export const useDistircts = defineStore('districts', {
    state: () =>({
        districts: []
    }),

    /**
     * Установка хранилища районов кадрового центра
     * @param {array} data 
     */
    setStore(data){
        this.districts = data
    }
})