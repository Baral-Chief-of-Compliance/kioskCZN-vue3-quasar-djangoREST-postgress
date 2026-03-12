<template>
    <div v-if="showRow" class="row bg-red">
        <div class="col">
            {{ props.titel }}
            {{ processTitel }}
        </div>
        <div class="col">
            {{ props.value }}
        </div>
    </div>
</template>

<script setup>
import { computed } from 'vue';


const showRow = computed(() => {
    switch(props.titel){
        case 'id': return false
        case 'vacancyName': return false
        case 'stateRegionCode': return false
        case 'codeProfessionalSphere': return false
        case 'socialProtecteds': return false
        case 'shift': return false
        case 'federalDistrictCode': return false
        case 'addressCode': return false
        case 'companyCode': return false
        case 'deleted': return false
        case 'visibility': return false
        case 'isPreferred': return false
        default: return true 

    }
})

const processTitel = computed(() => {
    switch(props.titel){
        case 'professionalSphereName': return 'Название профессиональной сферы'
        case 'vacancyAddress': return 'Адрес вакансии'
        case 'vacancyAddressAdditionalInfo': return 'Адресс доп. информация'
        case 'salary': return 'Зарплата'
        case 'salaryMin': return 'Минимальная зарплата'
        case 'salaryMax': return 'Максимальная зарплата'
        case 'languageKnowledge': return 'Знание языка'
        case 'busyType': return 'Тип занятости'
        case 'skills': return 'Навыки'
        default: return ''
    }
})

const props = defineProps({
    titel:{
        type: String,
        default: 'Наименование'
    },

    value: {
        type: String,
        default: 'Значение'
    }
})
</script>