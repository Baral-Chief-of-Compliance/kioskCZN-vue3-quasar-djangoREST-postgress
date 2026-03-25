<template>
    <div @click="useSearchingField" ref="searchField" class="col">
        <div :class="searchFieldClass">
            <div class="col-auto q-mr-md">
                <q-icon 
                    name="search" 
                    size="30px"
                    color="grey-7"
                />
            </div>
            <div
                :class="searchValueClass">
                {{ searchValue }}
            </div>
            <div class="col justify-end flex">
                <q-icon
                    v-if="showBackSpaceAll"
                    @click="backSpaceAll"
                    size="30px"
                    color="grey-7"
                    name="close"
                />
            </div>
        </div>
        <q-popup-proxy
            @hide="closeKeyboard"
            transition-show="scale"
            transition-hide="scale"
            :breakpoint="0"
            :offset="[-50, 0]"
        >
            <keyboard-component 
                v-model="searchValue"
            />
        </q-popup-proxy>
    </div>
</template>

<script setup>
import { computed, ref, useTemplateRef, watch } from 'vue';
import { useElementSize } from '@vueuse/core';
import { useVacanciesStore } from 'src/stores/vacancies';
import { useDistircts } from 'src/stores/districts';
import { getVacancies } from 'src/axios/vacancies';

import KeyboardComponent from './keyboard/KeyboardComponent.vue';



const vacancieStore = useVacanciesStore()
const districtsStore = useDistircts()

const active = ref(false)
const searchValue = ref('Найти...')

const searchField = useTemplateRef('searchField')
const { height: searchFieldHeight } = useElementSize(searchField)

const model = defineModel(0)


const searchFieldClass = computed(() => ({
    'row': true,
    'search-input': true,
    'active soft-glow': active.value,
    'inactive': !active.value,
}))

const searchValueClass = computed(() => ({
    'col-10 justify-start content-center flex search-text': true,
    'st-active': active.value,
    'st-inactive text-grey': !active.value,
}))

const showBackSpaceAll = computed(() => {
    if (searchValue.value === 'Найти...' || searchValue.value.length === 0){
        return false
    }else{
        return true
    }
})

const backSpaceAll = () => {
    searchValue.value = ''
}

watch(searchFieldHeight, (newValue) => {
    model.value = newValue
})

const timerId = ref(null) //Таймер для поиска

watch(searchValue, async(newValue) => {
    if (newValue != 'Найти...' && newValue.length > 0){
        if (timerId.value !=null){
            clearTimeout(timerId.value)
        }

        timerId.value = setTimeout(async() => {
            vacancieStore.loading = true
            vacancieStore.vacancieName = newValue
            vacancieStore.currentPage = 1
            const vacanciesRes = await getVacancies(
                districtsStore.districtMinCode,
                districtsStore.districtMaxCode,
                vacancieStore.currentPage,
                vacancieStore.vacancieName
            )
            if (vacanciesRes.status != 200){
                return;
            }
            vacancieStore.currentPage = vacanciesRes.data.current_page
            vacancieStore.count = vacanciesRes.data.count
            vacancieStore.pages = vacanciesRes.data.total_pages

            vacancieStore.setVacancies(vacanciesRes.data.results)

            vacancieStore.loading = false
        }, 300)
    }
})

const useSearchingField = () => {
    active.value = !active.value
    if (active.value){
        if (searchValue.value === 'Найти...'){
            searchValue.value = ''
        }
    }
}

const closeKeyboard = () => {
    if (active.value){
        active.value = false
    }
}

</script>

<style scoped>
    .search-input{
        border-radius: 15px;
        padding: 20px;
    }

    .active{
        border: 4px solid var(--q-indigo);
    }

    .inactive{
        border: 4px solid var(--q-blue-4);
    }

    .soft-glow {
        background: #fff;
        box-shadow: 0 0 20px 10px rgba(0, 0, 0, 0.1);
        border-radius: 12px;
        padding: 20px;
    }

    .search-text{
        font-size: 16px;
    }

    .st-active {
        font-weight: 500;
        color: var(--q-dark);
    }

    .st-inactive {
        font-weight: 400;
    }
</style>