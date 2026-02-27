<template>
    <q-page>
        <titel-page titel="Сотрудники" />
        <loading-spinner v-if="loading" :height="loadingHeight" />
        
        <div v-else-if="!loading && departmentsStore.departments.length > 0" class="row q-mt-lg q-mx-md">
            <div class="col-4">
                <scroll-area
                    :height="loadingHeight"
                >
                    <service-card 
                        class="q-mr-xl"
                        v-for="(dep, index) in departmentsStore.departments"
                        v-bind:key="dep.id"
                        :titel="dep.name"
                        @click-card="servicesStore.setActiveService(index)"
                    />
                </scroll-area>
            </div>
        </div>

        <not-found-content v-else :height="loadingHeight" />
    </q-page>
</template>

<script setup>
import { onMounted, ref, inject, computed } from 'vue';
import { getDepartments } from 'src/axios/departments';
import { useDepartments } from 'src/stores/departments';
import { usePCStore } from 'src/stores/personalCenter';
import { useWindowSize } from '@vueuse/core';


import TitelPage from 'src/components/TitelPage.vue';
import NotFoundContent from 'src/components/NotFoundContent.vue';
import LoadingSpinner from 'src/components/LoadingSpinner.vue';
import ScrollArea from 'src/components/ScrollArea.vue';
import ServiceCard from 'src/components/ServiceCard.vue';


const departmentsStore = useDepartments()
const pcStore = usePCStore()

const loading = ref(true)

const headerHeight = inject('headerHeight')
const {height: windowHeight } = useWindowSize()

const loadingHeight = computed(() => {
    return  `${windowHeight.value - headerHeight.value}px`
})

onMounted(async () => {
    loading.value = true
    if (pcStore.pcId != null){
        const res = await getDepartments(pcStore.pcId)

        if (res.status != 200){
            return;
        }

        departmentsStore.departments = res.data
    }
    loading.value = false
})


</script>