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
                    {{ processValue }}
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

const dataFormatNameValue = [
    'datePublished', 'changeTime' 
]

const dictValueName = [
    'requiredDriveLicense', 'languageKnowledge',
    'skills', 'hardSkills', 'softSkills'
]

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

const processValue = computed(() => {
    if (typeof props.value !== 'boolean'){
        if (dataFormatNameValue.includes(props.titel)){
            const date = new Date(props.value); 
            const ruDate = new Intl.DateTimeFormat('ru-RU').format(date);
            return ruDate;
        }else if (dictValueName.includes(props.titel)) {
            if (props.value.length == 0){
                return 'Не требуются'
            }else{
                return props.value
            }
        }else{
            return props.value
        }
    }else{
        return props.value
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
        color: var(--q-dark);
    }

    .info-value{
        color: var(--q-dark);
        font-size: 16px;
        font-weight: 500;
        line-height: 1.5;
        word-break: break-word;
    }
</style>