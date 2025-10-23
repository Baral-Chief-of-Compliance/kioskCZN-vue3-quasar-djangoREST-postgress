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
                        v-bind:key="index"
                        :titel="s.services_name"
                    />
                </scroll-area>
            </div>
            <div class="col-8">
                <service-name :label="servicesStore.activeService.services_name" class="q-mb-sm" />
                <scroll-area height="400px">
                <!-- {{ servicesStore.activeService }} -->
                <service-description :raw-html="servicesStore.activeService.services_description" class="q-mr-xl" />                
                </scroll-area>

                <scroll-area class="q-mt-xl" height="380px">
                    <service-emploeyr
                        class="q-mr-xl"
                        v-for="(emp, index) in servicesStore.activeService?.employees"
                        v-bind:key="index"
                        :name="emp.full_name"
                        :floor="emp.floor"
                        :room="emp.room"
                        :post="emp.post"
                    />
                </scroll-area>
            </div>
        </div>
        <notification-empty v-else />
    </q-page>
</template>

<script setup>

import ScrollArea from 'src/components/ScrollArea.vue';
import TitelPage from 'src/components/TitelPage.vue';
import { useServicesStore } from 'src/stores/services';
import NotificationEmpty from 'src/components/NotificationEmpty.vue';
import ServiceCard from 'src/components/ServiceCard.vue';
import ServiceName from 'src/components/ServiceName.vue';
import ServiceDescription from 'src/components/ServiceDescription.vue';
import ServiceEmploeyr from 'src/components/ServiceEmploeyr.vue';



const servicesStore = useServicesStore()



</script>