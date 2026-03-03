<template>
    <q-page>
        <titel-page titel="Вакансии" />
        <loading-spinner v-if="loading" :height="loadingHeight" />

        <div v-else-if="!loading && districtsStore.districts.length > 0" class="q-mt-lg q-mx-md">
            <scroll-area :height="districtsHeight">
                <div class="row justify-between">
                    <card-menu
                        v-for="d in districtsStore.districts"
                        v-bind:key="d.id"
                        :titel="d.name"
                        for-districts
                        :work-place-count="d.count_vacansy"
                    />
                </div>
            </scroll-area>
        </div>
        <not-found-content v-else :height="loadingHeight" />
    </q-page>
</template>

<script setup>
import { onMounted, onUnmounted, ref, inject, computed } from 'vue';
import { useWindowSize } from '@vueuse/core';

import TitelPage from 'src/components/TitelPage.vue';
import NotFoundContent from 'src/components/NotFoundContent.vue';
import { usePCStore } from 'src/stores/personalCenter';
import { useDistircts } from 'src/stores/districts';
import LoadingSpinner from 'src/components/LoadingSpinner.vue';
import ScrollArea from 'src/components/ScrollArea.vue';
import { getDistricts } from 'src/axios/districts';
import CardMenu from 'src/components/CardMenu.vue';


const pcStore = usePCStore()
const districtsStore = useDistircts()

const loading = ref(true)

const headerHeight = inject('headerHeight')
const {height: windowHeight } = useWindowSize()

const loadingHeight = computed(() => {
    return  `${windowHeight.value - headerHeight.value}px`
})

const districtsHeight = computed(() => {
    return  `${windowHeight.value - (headerHeight.value + 80)}px`
})

//Получить районы мурманской области с числок рабочих мест
const getDistirctsFromBack = async() => {
    loading.value = true

    if (pcStore.pcId != null){

        const res = await getDistricts()

        if (res.status != 200){
            return;
        }

        districtsStore.districts = res.data
    }

    loading.value = false
}

let unsubscribePCStoreAction = pcStore.$onAction(
    ({name, after }) => {
        after(async() => {
            if (name === 'setStore'){
                await getDistirctsFromBack()
            }
        })
    }
)

onMounted(async () => {
    await getDistirctsFromBack()
})


onUnmounted(() => {
    if (unsubscribePCStoreAction){
        unsubscribePCStoreAction()
    }
})

</script>