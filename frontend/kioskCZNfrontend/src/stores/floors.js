import { defineStore } from "pinia";

export const useFloorsStore = defineStore('floors', {
    state: () => ({
        floors: [],
        activeFloorIndex: 0,
    }),

    getters: {
        getFloors: (state) => state.floors
    },

    actions: {
        setStore(data){
            this.floors = data
        },

        /**
         * Выбрать index активного этажа из представленных
         * @param {number} index 
         */
        setActiveFloor(index){
            if (this.floors.length > 0){
                if (index < this.floors.length){
                    this.activeFloorIndex = index
                }
            }
        }
    }
})