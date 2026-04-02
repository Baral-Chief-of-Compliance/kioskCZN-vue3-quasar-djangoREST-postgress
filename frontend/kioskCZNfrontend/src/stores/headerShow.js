import { defineStore } from "pinia";

export const useHeaderShowState = defineStore('headerShowStore', {
    state: () => ({
        show: true
    }),

    actions: {
        /**
         * Показать header
         */
        showHeader(){
            this.show = true
        },

        hideHeader(){
            this.show = false
        }
    }
})