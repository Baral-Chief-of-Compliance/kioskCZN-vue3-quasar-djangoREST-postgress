<template>
    <div>
        <q-separator class="q-mb-lg"></q-separator>
        <div class="row">

            <div class="col text-center">
                <div class="info-titel">Вакансия</div>
                <qr-code width="400px" :url="props.vacancyUrl" />
            </div>
            <div class="col text-center">
                <div class="info-titel">Работодатель</div>
                <qr-code width="400px" :url="props.url" />
            </div>
        </div>
    </div>
</template>

<script setup>
import QrCode from './QrCode.vue';

const props = defineProps({
    vacancyUrl:{ //Ссылка на вакансию
        type: String,
        default: 'https://trudvsem.ru/'
    },

    url: { //Ссылка на работодателя
        type: String,
        default: 'https://trudvsem.ru/'
    }
})
</script>


<style scoped>
    .info-titel{
        font-weight: 600;
        letter-spacing: .2px;
        font-size: 24px;
        line-height: 1.4;
        color: #25282b;
    }

</style>