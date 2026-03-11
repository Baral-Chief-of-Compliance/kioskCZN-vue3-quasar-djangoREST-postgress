<template>
    <q-page>
        <titel-page titel="Навигатор мер поддержки" />
        <loading-spinner :height="loadingHeight" v-if="loading" />
        <div class="row q-mt-lg q-mx-md" v-else-if="!servicesStore.getEmptyStatus && !loading">
            <div class="col-4">
                <scroll-area
                    height="850px"
                >
                    <service-card
                        class="q-mr-xl"
                        v-for="(s, index) in servicesStore.getServices"
                        @click-card="servicesStore.setActiveService(index)"
                        :active="index === servicesStore.activeServiceIndex"
                        v-bind:key="s.id"
                        :titel="s.name"
                    />
                </scroll-area>
            </div>
            <div class="col-8">
                <service-name 
                    :label="servicesStore.activeService.name" 
                    class="q-mb-sm" 
                    v-model="serviceTitelHeight"
                />
                <scroll-area :height="serviceTextHeight">
                <service-description :raw-html="servicesStore.activeService.description" class="q-mr-xl q-ml-md" />                
                </scroll-area>

                <scroll-area v-if="
                    !activeServiceWorkersLoading && 
                    servicesStore.activeServiceWorkers.length > 0 && showWorker
                    " 
                    class="q-mt-xl" 
                    height="380px"
                >
                    <service-emploeyr
                        class="q-mr-xl q-ml-md"
                        v-for="(emp, index) in servicesStore.activeServiceWorkers"
                        v-bind:key="index"
                        :name="emp.fio"
                        :floor="emp.floor"
                        :room="emp.room_name"
                        :room-id="emp.room_id"
                        :post="emp.post_name"
                    />

                </scroll-area>

                <div v-else-if="activeServiceWorkersLoading && showWorker">
                    <loading-spinner height="400px" />
                </div>

                <empty-block-info text="Ой, на сегодня нет сотрудников, которые предоставляют данную меру поддержки..." v-else-if="showWorker" />
            </div>
        </div>
        <notification-empty v-else />
    </q-page>
</template>

<script setup>
import { onMounted, watch, ref, inject, computed } from 'vue';

import { useWindowSize } from '@vueuse/core';

import ScrollArea from 'src/components/ScrollArea.vue';
import TitelPage from 'src/components/TitelPage.vue';
import { useServicesStore } from 'src/stores/services';
import NotificationEmpty from 'src/components/NotificationEmpty.vue';
import ServiceCard from 'src/components/ServiceCard.vue';
import ServiceName from 'src/components/ServiceName.vue';
import ServiceDescription from 'src/components/ServiceDescription.vue';
import ServiceEmploeyr from 'src/components/ServiceEmploeyr.vue';
import ServicesService from 'src/axios/services';
import { usePCStore } from 'src/stores/personalCenter';
import LoadingSpinner from 'src/components/LoadingSpinner.vue';
import EmptyBlockInfo from 'src/components/EmptyBlockInfo.vue';


const showWorker = ref(false)
const loading = ref(true)
const serviceTitelHeight = ref(0)

const headerHeight = inject('headerHeight')
const {height: windowHeight } = useWindowSize()

const loadingHeight = computed(() => {
    return  `${windowHeight.value - headerHeight.value}px`
})

const serviceTextHeight = computed(() => {
    return  `${windowHeight.value - (headerHeight.value + serviceTitelHeight.value + 120)}px`
})

const servicesStore = useServicesStore()
const pcStore = usePCStore()

const activeServiceWorkersLoading = ref(true)


const getServices = async() => {
    loading.value = true
    const res = await ServicesService.getAll();

    if (res.status != 200){
        return;
    }

    servicesStore.setStore(
        res.data
    )

    loading.value = false
}

onMounted(async() => {
    await getServices()
})

watch(() => servicesStore.activeService, async (service) => {
    activeServiceWorkersLoading.value = true
    const workers = await ServicesService.getServiceWorkers(
        service.id,
        pcStore.pcId
    )

    servicesStore.setActiveServiceWorkers(workers)
    activeServiceWorkersLoading.value = false
})


</script>