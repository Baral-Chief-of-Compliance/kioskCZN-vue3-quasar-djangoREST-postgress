import { defineStore } from "pinia";

export const useFloorsStore = defineStore('floors', {
    state: () => ({
        floors: [],
        activeFloorIndex: 0,
        activeRoom: null
    }),

    getters: {
        getFloors: (state) => state.floors,

        /**
         * Возвращает url на схему активного этажа
         * @param {object} state 
         * @returns {string}
         */
        getActiveFloorImg (state){
            if (state.floors.length > 0){
                return state.floors[state.activeFloorIndex].building_img
            }else{
                return null
            }
        },

        /**
         * Получить список комнат с активного этажа кадрового центра
         * @param {object} state 
         * @returns {array}
         */
        getActiveFloorRooms(state){
            if (state.floors.length > 0){
                return state.floors[state.activeFloorIndex].rooms
            }else{
                return []
            }
        },

        /**
         * Получить список работников активного кабинета кадрового центра
         * @param {object} state 
         * @returns {array}
         */
        getActiveRoomWorkers(state){
            if (state.activeRoom != null){
                return state.activeRoom.workers
            }else{
                return []
            }
        },

        /**
         * Получить наименование активного кабинета кадрового центра
         * @param {object} state 
         * @returns {string}
         */
        getActiveRoomName(state){
            if (state.activeRoom != null){
                return state.activeRoom.name
            }else{
                return 'Наименование кабинета'
            }
        }
    },

    actions: {
        setStore(data){
            this.activeFloorIndex = 0;
            this.floors = data;
        },

        /**
         * Выбрать index активного этажа из представленных
         * @param {number} index 
         */
        setActiveFloor(index){
            if (this.floors.length > 0){
                if (index < this.floors.length){
                    this.activeFloorIndex = index
                    this.setActiveRoom()
                }
            }
        },

        setActiveRoom(id=0){
            if (this.floors.length > 0){
                if (this.floors[this.activeFloorIndex].rooms.length > 0){
                    if (id != 0){
                        const room = this.floors[this.activeFloorIndex].rooms.find(r => r.id === id)
                        if (room){
                            this.activeRoom = room
                        }
                    }else{
                        const room = this.floors[this.activeFloorIndex].rooms[0]
                        if (room){
                            this.activeRoom = room
                        }
                    }
                }else{
                    this.activeRoom = null
                }
            }else{
                this.activeRoom = null
            }
        }
    }
})