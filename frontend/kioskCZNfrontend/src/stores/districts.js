import { defineStore } from "pinia";

export const useDistircts = defineStore('districts', {
    state: () =>({
        districts: [],
        districtId: null,
        districtName: 'Наименование района',
        districtMinCode: null,
        districtMaxCode: null,
        loading: true
    }),

    /**
     * Установка хранилища районов кадрового центра
     * @param {array} data 
     */
    setStore(data){
        this.districts = data
    }
})