import { defineStore } from "pinia";

export const useYandexApiKeyStore = defineStore('yandexApiKey',{
    state: () => ({
        key: null
    }),

    getters: {
        getSettingsForYandex(state){
            return {
                apiKey: state.key,
                suggestApiKey: '',
                lang: 'ru_RU',
                coordorder: 'latlong',
                enterprise: false,
                version: '2.1'
            }
        }
    },

    actions: {
        /**
         * Установить занчение активного ключа Яндекс карт
         * @param {object} data 
         */
        setKey(data){
            if ('key' in data){
                    if (data.key.length > 0){
                        this.key = data.key
                        return;
                    }
            }

            this.key = null
        }
    }
})