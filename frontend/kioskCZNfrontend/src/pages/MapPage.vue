<template>
    <q-page>
        <titel-page titel="Карта здания" />
        <loading-spinner v-if="loading" :height="loadingHeight" />
        <div v-else-if="!loading && floorsStore.floors.length > 0">
            <div class="row justify-center">
                <q-btn 
                    size="lg"
                    unelevated
                    :label="f.number + ' этаж'"
                    v-for="(f, index ) in floorsStore.floors"
                    v-bind:key="f.id"
                    :class="floorBtnClass(index)"
                    @click="floorsStore.setActiveFloor(index)"
                />
            </div>
        </div>
        <not-found-content v-else :height="loadingHeight" />
    </q-page>
</template>

<script setup>
import { onMounted, onUnmounted, ref, inject, computed } from 'vue';
import { useWindowSize } from '@vueuse/core';

import { usePCStore } from 'src/stores/personalCenter';
import { useFloorsStore } from 'src/stores/floors';
import { getFloorsFromPC } from 'src/axios/floors';
import TitelPage from 'src/components/TitelPage.vue';
import NotFoundContent from 'src/components/NotFoundContent.vue';
import LoadingSpinner from 'src/components/LoadingSpinner.vue';


const floorsStore = useFloorsStore()
const pcStore = usePCStore()

const loading = ref(true)

const headerHeight = inject('headerHeight')
const {height: windowHeight } = useWindowSize()

const loadingHeight = computed(() => {
    return  `${windowHeight.value - headerHeight.value}px`
})


//Получить этажи кадрового центра
const getPCFloors = async() => {
    loading.value = true
    if (pcStore.pcId != null){
        const res = await getFloorsFromPC(pcStore.pcId)

        if (res.status != 200){
            return;
        }

        floorsStore.setStore(res.data)
    }
    loading.value = false
}


let unsubscribePCStoreAction = pcStore.$onAction(
    ({name, after }) => {
        after(async() => {
            if (name === 'setStore'){
                await getPCFloors()
            }
        })
    }
)

const floorBtnClass = computed(() => {
    return (index) => ({
        'floor-btn': true, 
        'q-px-lg': true,
        'q-py-sm': true,
        'q-mx-xl': true,
        'q-mt-lg': true,
        'text-white': floorsStore.activeFloorIndex === index,
        'bg-orange': floorsStore.activeFloorIndex === index,
        'text-indigo': floorsStore.activeFloorIndex != index,
        'bg-white': floorsStore.activeFloorIndex != index,
    })

})


onMounted(async () => {
    await getPCFloors()
})


onUnmounted(() => {
    if (unsubscribePCStoreAction){
        unsubscribePCStoreAction()
    }
})
</script>

<style scoped>
    .floor-btn{
        border-radius: 10px !important;
    }
</style>