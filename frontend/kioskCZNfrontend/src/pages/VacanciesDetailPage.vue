<template>
    <q-page>
        <titel-page 
            :path-name="VACANCIES"
            :titel="districtsStore.getName"
        />
        <loading-spinner v-if="loading" :height="loadingHeight"/>
        <empty-block-info 
            v-else-if="!loading && vacanciesStore.vacancies.length == 0"
            :height="loadingHeight"
            text="Ой, не удалось найти вакансии..."
        />
        <div v-else class="q-mt-lg q-mx-md row">
            <control-weeks-btn 
                :disable="vacanciesStore.currentPage === 1" 
                left 
                @click="goPreviousPage"
            />
            <div class="col">
                <search-vacancie-field />
                <scroll-area :height="scrollHeght">
                    <div class="row justify-between q-mx-xl">
                        <vacancie-card 
                            v-for="v in vacanciesStore.vacancies"
                            v-bind:key="v.id"
                            :id="v.id"
                            :name="v.vacancyName"
                            :salary="v.salary"
                            :salary-min="v.salaryMin"
                            :salary-max="v.salaryMax"
                            :work-places="v.workPlaces"
                            :address="v.vacancyAddress"
                        />
                    </div> 
                </scroll-area>
                <vacansy-page-info class="q-mt-md"
                    :count="vacanciesStore.count"
                    :work-places="districtsStore.workPlaces"
                    :current-page="vacanciesStore.currentPage"
                    :pages="vacanciesStore.pages"
                />
            </div>
            <control-weeks-btn
                :disable="vacanciesStore.currentPage === vacanciesStore.pages" 
                @click="goNextPage"
            />

        </div>

    </q-page>
</template>

<script setup>
import { ref, inject, computed, onMounted, onUnmounted } from 'vue';

import { useWindowSize } from '@vueuse/core';
import { useRoute } from 'vue-router';

import TitelPage from 'src/components/TitelPage.vue';
import LoadingSpinner from 'src/components/LoadingSpinner.vue';
import { useDistircts } from 'src/stores/districts';
import { VACANCIES } from 'src/router/pathName';
import { getDistrictDetail } from 'src/axios/districts';
import { usePCStore } from 'src/stores/personalCenter';
import { useVacanciesStore } from 'src/stores/vacancies';
import { getVacancies } from 'src/axios/vacancies';
import EmptyBlockInfo from 'src/components/EmptyBlockInfo.vue';
import VacancieCard from 'src/components/VacancieCard.vue';
import ScrollArea from 'src/components/ScrollArea.vue';
import ControlWeeksBtn from 'src/components/btns/ControlWeeksBtn.vue';
import VacansyPageInfo from 'src/components/VacansyPageInfo.vue';
import SearchVacancieField from 'src/components/vacancie/SearchVacancieFIeld.vue'


const route = useRoute()

const districtsStore = useDistircts()
const vacanciesStore = useVacanciesStore()
const pcStore = usePCStore()


const {height: windowHeight} = useWindowSize()
const headerHeight = inject('headerHeight')

const loadingHeight = computed(() => {
    return  `${windowHeight.value - headerHeight.value}px`
})

const scrollHeght = computed(() => {
    return  `${windowHeight.value - (headerHeight.value + 150)}px`
})

const loading = ref(true)


const getVacansyFromDistrict = async() => {
    loading.value = true

    if (pcStore.pcId != null && route.params.district_id != null){
        const res = await getDistrictDetail(route.params.district_id)

        if (res.status != 200){
            return;
        }

        districtsStore.districtId = res.data.id
        districtsStore.districtName = res.data.name
        districtsStore.districtMinCode = res.data.min_code
        districtsStore.districtMaxCode = res.data.max_code
        districtsStore.workPlaces = res.data.count_vacansy

        const vacanciesRes = await getVacancies(
            districtsStore.districtMinCode,
            districtsStore.districtMaxCode,
            vacanciesStore.currentPage
        )


        if (vacanciesRes.status != 200){
            return;
        }

        vacanciesStore.currentPage = vacanciesRes.data.current_page
        vacanciesStore.count = vacanciesRes.data.count
        vacanciesStore.pages = vacanciesRes.data.total_pages
        if (vacanciesStore.pages > vacanciesStore.currentPage){
            vacanciesStore.nextPage = vacanciesStore.currentPage + 1
        }

        if (vacanciesStore.currentPage > 1){
            vacanciesStore.previousPage = vacanciesStore.currentPage - 1
        }

        vacanciesStore.setVacancies(vacanciesRes.data.results)
    }


    loading.value = false
}

const goNextPage = async() => {
    if (vacanciesStore.currentPage < vacanciesStore.pages){
        vacanciesStore.currentPage ++
        await getVacansyFromDistrict()
    }
}

const goPreviousPage = async() => {
    if(vacanciesStore.currentPage > 1){
        vacanciesStore.currentPage --
        await getVacansyFromDistrict()
    }
}

let unsubscribePCStoreAction = pcStore.$onAction(
    ({name, after }) => {
        after(async() => {
            if (name === 'setStore'){
                await getVacansyFromDistrict()
            }
        })
    }
)


onMounted(async() => {
    await getVacansyFromDistrict()
})

onUnmounted(() => {
    if (unsubscribePCStoreAction){
        unsubscribePCStoreAction()
    }
    vacanciesStore.$reset()
})
</script>