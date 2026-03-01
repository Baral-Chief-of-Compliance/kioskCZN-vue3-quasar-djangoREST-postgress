import { defineStore } from "pinia";

export const useEventStore = defineStore('events', {
    state: () => ({
        events: []
    }),

    gettes: {
        getEvents: (state) => state.events
    },

    actions: {
        setStore(data){
            this.events = data
        }
    }
})