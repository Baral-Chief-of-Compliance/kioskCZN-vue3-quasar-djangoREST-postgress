<template>
    <q-btn 
        icon="filter_alt"
        rounded
        :color="colorBtn"
        unelevated
        :outline="outLineBtn"
        class="q-px-lg"
    />
</template>

<script setup>
import { computed } from 'vue';
import { useVacanciesStore } from 'src/stores/vacancies';

const vacancieStore = useVacanciesStore()

const colorBtn = computed(() => {
    if (vacancieStore.filter){
        return 'indigo'
    }else{
        return 'blue'
    }
})

const outLineBtn = computed(() => {
    if (vacancieStore.filter){
        return false
    }else{
        return true
    }
})

</script>