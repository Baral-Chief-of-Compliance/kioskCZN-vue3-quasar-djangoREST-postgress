import { defineStore } from "pinia";


export const HEAD_INFO_PAGE = 0
export const PC_INFO_PAGE = 1
export const SOCIAL_NETWORK_PAGE = 2

export const usePCInfoStore = defineStore('personalCenterInfo', {
    state: () => ({
        id: null,
        socialNetworks: [],
        address: [],
        phones: [],
        emails: [],
        sites: [],
        timeTables: [],
        headInfo: null,
        parentOrg: null,

        activePage: HEAD_INFO_PAGE
    }),

    actions: {
        /**
         * Настройка харнилища информации о кадровом центре
         * @param {object} data 
         */
        setStore(data){
            this.id = data.id
            this.socialNetworks = data.social_networks
            this.address = data.address
            this.phones = data.phones
            this.emails = data.emails
            this.sites = data.sites
            this.timeTables = data.timetables
            this.headInfo = data.head_info
            this.parentOrg = data.parent_org
        }
    }
})