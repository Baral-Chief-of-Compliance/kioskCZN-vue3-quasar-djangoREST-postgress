import { defineStore } from "pinia";


export const useVacanciesStore = defineStore('vacancies', {
    state: () => ({
        vacancies: [],
        currentPage: 1,
        nextPage: null,
        previousPage: null,
        pages: 0,
        count: 0,
    }),

    actions: {
        /**
         * Установить вакансии в store
         * @param {object} data 
         */
        setVacancies(data){
            this.vacancies = data
        }
    }
})