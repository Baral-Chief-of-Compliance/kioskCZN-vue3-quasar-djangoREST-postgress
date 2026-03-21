<template>
    <div>
        <vacancie-row-info 
            titel="vacancyAddress"
            :value="props.vacancyAddress"
            in-map
        />
        <vacancie-row-info 
            titel="vacancyAddressAdditionalInfo"
            :value="props.vacancyAddressAdditionalInfo"
            in-map
        />
        <div class="flex justify-center">
            <div :style="mapStyle">
            <yandex-map
                :settings="settings"
                :coordinates="mapCenter"
                :zoom="zoom"
                style="width: 100%; height: 100%;"
                :controls="[]"
            >
                <!-- Маркер с координатами из props -->
                        <yandex-marker
                            type="Point"
                            :marker-id="123"
                            :coordinates="mapCenter" 
                        />
            </yandex-map>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { YandexMap, YandexMarker } from 'vue-yandex-maps';
import VacancieRowInfo from './VacancieRowInfo.vue';
import { useYandexApiKeyStore } from 'src/stores/yandexApiKeys';

const yaAPIKeyStore = useYandexApiKeyStore()


const props = defineProps({
    latitude: { // Широта
        type: Number,
        default: 68.9667
    },
    longitude: { // Долгота
        type: Number,
        default: 33.0833
    },
    vacancyAddress: {
        type: String,
        default: 'Адрес'
    },
    vacancyAddressAdditionalInfo: {
        type: String,
        default: 'Полный адрес'
    },
    width: {
        type: String,
        default: '800px'
    }
})

// Вычисляемое свойство для центра карты и позиции маркера
const mapCenter = computed(() => [props.latitude, props.longitude])

const zoom = ref(17)

const settings = {
  apiKey: yaAPIKeyStore.apiKey,
  lang: 'ru_RU',
  coordorder: 'latlong',
  debug: false,
  version: '2.1'
}

const mapStyle = computed(() => ({
    width: props.width,
    height: '600px'
}))
</script>