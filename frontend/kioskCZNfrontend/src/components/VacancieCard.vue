<template>
    <q-card class="no-shadow vacansy-card q-mb-md">
        <q-card-section>
            <div class="vacansy-card-name">{{ props.name }}</div>
            <div class="q-mt-xs vacansy-card-address">{{ props.address }}</div>
            <div class="q-mt-sm vacansy-card-salary">{{ props.salary }}</div>
        </q-card-section>
    </q-card>
</template>

<script setup>

const props = defineProps({
    id:{
        type: String,
        default: '547df4f9-e52b-11ef-9a52-e7d0d2cf29b1'
    },
    name: {
        type: String,
        default: 'Наименование вакансии'
    },
    salary: {
        type: String,
        default: 'от 60000'
    },
    address:{
        type: String,
        default: 'Адрес'
    },
    salaryMin: {
        type: Number,
        default: 0
    },
    salaryMax: {
        type: Number,
        default: 1
    },
    workPlaces: {
        type: Number,
        default: 1
    }

})

</script>

<style scoped>
    .vacansy-card{
        width: 385px;
        height: 172px;
        border-radius: 10px !important;
        border: 1px solid #e8e8e8;
    }

    .vacansy-card-name{
        color: #25282b;
        line-height: 1.25;
        font-weight: 600;
        font-size: 16px;
        word-break: break-word;
    }

    .vacansy-card-salary{
        font-size: 16px;
        line-height: 1.5;
        color: #25282b;
    }

    .vacansy-card-address{
        font-size: 14px;
        line-height: 1.286;
        color: #25282b; 
    }

</style>