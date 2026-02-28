import { defineStore } from "pinia";

export const useDepartments = defineStore('departments', {
    state: () => ({
        departments: [],
        activeDepartmentsIndex: 0
    }),

    getters: {
        getDepartments: (state) => state.departments,
        /**
         * Получить список сотрудников аткивного отдела
         * @param {object} state 
         * @returns {array} - список сотрудников
         */
        getWorkersFromActiveDep(state){
            if (state.departments.length > 0){
                return state.departments[state.activeDepartmentsIndex].workers
            }else{
                return []
            }
        },

        /**
         * Получить наименование активного отедла
         * @param {object} state 
         * @returns {string}
         */
        getActiveDepartmentName(state){
            if (state.departments.length > 0){
                return state.departments[state.activeDepartmentsIndex].name
            }else{
                return 'Наименование активного отдела'
            }
        }
    },

    actions: {

        /**
         * Установка хранилища отделов кадрового центра
         * @param {array} data 
         */
        setStore(data){
            this.departments = data?.departments
        },

        /**
         * Выбрать index активного отдела из представленных 
         * @param {number} index 
         */
        setActiveDepartment(index){
            if (this.departments.length > 0){
                if (index < this.departments.length){
                    this.activeDepartmentsIndex = index
                }
            }
        }
    }
})