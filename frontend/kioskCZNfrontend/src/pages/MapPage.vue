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

            <div class="flex flex-center q-mt-xl" style="position: relative;">
                <card-info-room 
                    v-if="floorsStore.activeRoom"
                    :name="floorsStore.getActiveRoomName"
                    :workers="floorsStore.getActiveRoomWorkers"
                />
                <img
                style="height: 776px; width: 1000px; display: block;"
                :src="floorsStore.getActiveFloorImg"
                usemap="#pc-map"
                />

                <svg
                    viewBox="0 0 1000 776"
                    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none;"
                >
                <polygon
                    v-if=" floorsStore.activeRoom"
                    :points=" floorsStore.activeRoom.vector_info"
                    fill="rgba(255, 0, 0, 0.3)"
                    stroke="red"
                    stroke-width="2"
                />
                </svg>

                <map name="pc-map">
                <area
                    v-for="r in floorsStore.getActiveFloorRooms"
                    v-bind:key="r.id"
                    shape="poly"
                    :coords="r.vector_info"
                    :alt="r.name"
                    @click="setActiveRoom(r)"
                >
                </map>
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
import CardInfoRoom from 'src/components/CardInfoRoom.vue';


const floorsStore = useFloorsStore()
const pcStore = usePCStore()

const loading = ref(true)

const headerHeight = inject('headerHeight')
const {height: windowHeight } = useWindowSize()

const loadingHeight = computed(() => {
    return  `${windowHeight.value - headerHeight.value}px`
})


const props = defineProps({
    activeRoomId: {
        type: Number,
        default: 0
    },
    activeFloor: {
        type: Number,
        default: 0
    }
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

        // проверка если в params параметры этажа и кабинета,
        // которые необходимо отобразить
        if (props.activeFloor != 0){
            floorsStore.findFloor(props.activeFloor)
        }

        if(props.activeRoomId != 0){
            floorsStore.setActiveRoom(props.activeRoomId)
        }

        if (floorsStore.activeRoom === null){
            floorsStore.setActiveRoom()
        }
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

const setActiveRoom = (room) => {
    floorsStore.activeRoom = room
}


onMounted(async () => {
    await getPCFloors()
})


onUnmounted(() => {
    floorsStore.$reset()
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