<template>
    <div v-if="showRow" class="q-mb-lg" style="min-height: 40px;">
        <div  class="row">
            <div class="col info-titel">
                {{ processTitel }}
            </div>
            <div class="col info-value">
                <div 
                    v-if="typeof props.value !== 'boolean' && props.value !== undefined"
                >
                    {{ props.value }}
                </div>
                <boolean-propery 
                    v-else
                    :value="props.value"
                />
            </div>
        </div>
        <q-separator></q-separator>
    </div>
</template>

<script setup>
import { computed } from 'vue';
import BooleanPropery from './BooleanPropery.vue';


const valueShow = {
    professionalSphereName: 'Сфера деятельности',
    salary: 'Зарплата',
    salaryMin: 'Минимальная зарплата',
    salaryMax: 'Максимальная зарплата',
    languageKnowledge: 'Знание языка',
    busyType: 'Тип занятости',
    skills: 'Навыки',
    workPlaceForeign: 'Место работы за рубежом',
    workPlaceOrdinary: 'Место работы обычное',
    workPlaceQuota: 'Место работы по квоте',
    workPlaceSpecial: 'Специальное место работы',
    trainingDays: 'Обучающий период (дни)',
    hardSkills: 'Профессиональные знания и умения',
    softSkills: 'Социально-психологические качества',
    experienceRequirements: 'Требуемый опыт',
    scheduleType: 'Тип занятости',
    careerPerspective: 'Карьерные перспективы',
    needMedcard: 'Медицинская книжка',
    sourceType: 'Тип вакансии',
    requiredDriveLicense: 'Водительские права',
    changeTime: 'Обновлено',
    contactPerson: 'Контактное лицо',
    fullCompanyName: 'Работодатель',
    workPlaces: 'Кол-во рабочих мест',
    isUzbekistanRecruitment: 'Узбекистан рекрутинг',
    datePublished: 'Дата публикации',
    accommodationCapability: 'Проживания',
    foreignWorkersCapability: 'Найм иностранных работников',
    isQuoted: 'Квота',
    responsibilities: 'Обязанности',
    regionName: 'Регион',
    status: 'Статус',
    educationType: 'Образование',
    inn: 'ИНН',
    kpp: 'КПП',
    ogrn: 'ОГРН',
    contactType: 'Способ связи',
    contactValue: 'Контактная информация',
    isModerated: 'Вакансия прошла модерацию'
}

const mapValueShow = {
    vacancyAddress: 'Адрес вакансии',
    vacancyAddressAdditionalInfo: 'Адресс доп. информация',
}
const showRow = computed(() => {
    if (props.inMap){
        return props.titel in mapValueShow
    }else{
        return  props.titel in valueShow
    }
})

const processTitel = computed(() => {
    if (props.inMap){
        if (props.titel in mapValueShow){
            return mapValueShow[props.titel]
        }else{
            return 'Свойство'
        }
    }else{
        if (props.titel in valueShow){
            return valueShow[props.titel]
        }else{
            return 'Свойство'
        }
    }
})

const props = defineProps({
    titel:{
        type: String,
        default: 'Наименование'
    },

    value: {
        default: 'Значение'
    },

    inMap: {
        type: Boolean,
        default: false
    }
})
</script>

<style scoped>
    .info-titel{
        font-weight: 600;
        letter-spacing: .2px;
        font-size: 20px;
        line-height: 1.4;
        color: #25282b;
    }

    .info-value{
        color: #25282b;
        font-size: 16px;
        font-weight: 500;
        line-height: 1.5;
        word-break: break-word;
    }
</style>