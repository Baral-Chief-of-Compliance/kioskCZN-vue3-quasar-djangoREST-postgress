<template>
    <q-page>
        <titel-page titel="Навигатор мер поддержки" />
        <div class="row q-mt-lg q-mx-md" v-if="!servicesStore.getEmptyStatus">
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
                <service-name :label="servicesStore.activeService.name" class="q-mb-sm" />
                <scroll-area height="400px">
                <service-description :raw-html="servicesStore.activeService.description" class="q-mr-xl q-ml-md" />                
                </scroll-area>

                <scroll-area v-if="
                    !activeServiceWorkersLoading && 
                    servicesStore.activeServiceWorkers.length > 0
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

                <div v-else-if="activeServiceWorkersLoading">
                    <loading-spinner height="400px" />
                </div>

                <empty-block-info text="Ой, на сегодня нет сотрудников, которые предоставляют данную меру поддержки..." v-else />
            </div>
        </div>
        <notification-empty v-else />
    </q-page>
</template>

<script setup>
import { onMounted, watch, ref } from 'vue';

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


const servicesStore = useServicesStore()
const pcStore = usePCStore()

const activeServiceWorkersLoading = ref(true)


onMounted(async() => {
    const services = await ServicesService.getAll()
    servicesStore.setStore(
        services
    )
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