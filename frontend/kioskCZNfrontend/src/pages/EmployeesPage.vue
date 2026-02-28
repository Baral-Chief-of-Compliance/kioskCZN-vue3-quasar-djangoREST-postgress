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
                        :active="index === departmentsStore.activeDepartmentsIndex"
                        @click-card="departmentsStore.setActiveDepartment(index)"
                    />
                </scroll-area>
            </div>

            <div class="col-8">
                <service-name 
                    :label="departmentsStore.getActiveDepartmentName"
                    class="q-mb-sm"
                />

                <scroll-area 
                    class="q-mt-xl"
                    v-if="departmentsStore.getWorkersFromActiveDep.length > 0"
                    :height="emploerListHeight"
                >
                    <service-emploeyr 
                        class="q-mr-xl q-ml-md"
                        v-for="(emp, index) in departmentsStore.getWorkersFromActiveDep"
                        v-bind:key="index"
                        :name="emp.fio"
                        :floor="emp.floor"
                        :room="emp.room_name"
                        :post="emp.post_name"
                    />
                </scroll-area>

                <not-found-content v-else :height="loadingHeight" />
            </div>
        </div>

        <not-found-content v-else :height="loadingHeight" />
    </q-page>
</template>

<script setup>
import { onMounted, onUnmounted, ref, inject, computed } from 'vue';
import { useWindowSize } from '@vueuse/core';

import { getDepartments } from 'src/axios/departments';
import { useDepartments } from 'src/stores/departments';
import { usePCStore } from 'src/stores/personalCenter';
import TitelPage from 'src/components/TitelPage.vue';
import NotFoundContent from 'src/components/NotFoundContent.vue';
import LoadingSpinner from 'src/components/LoadingSpinner.vue';
import ScrollArea from 'src/components/ScrollArea.vue';
import ServiceCard from 'src/components/ServiceCard.vue';
import ServiceName from 'src/components/ServiceName.vue';
import ServiceEmploeyr from 'src/components/ServiceEmploeyr.vue';


const departmentsStore = useDepartments()
const pcStore = usePCStore()

const loading = ref(true)

const headerHeight = inject('headerHeight')
const {height: windowHeight } = useWindowSize()

const loadingHeight = computed(() => {
    return  `${windowHeight.value - headerHeight.value}px`
})

const emploerListHeight = computed(() => {
    return  `${windowHeight.value - (headerHeight.value + 200)}px`
})

//Получить отделы кадрового центра
const getPCDepartments = async () => {
    loading.value = true
    if (pcStore.pcId != null){
        const res = await getDepartments(pcStore.pcId)

        if (res.status != 200){
            return;
        }

        departmentsStore.departments = res.data
    }
    loading.value = false
}

let unsubscribePCStoreAction = pcStore.$onAction(
    ({name, after }) => {
        after(async() => {
            if (name === 'setStore'){
                await getPCDepartments()
            }
        })
    }
)

onMounted(async () => {
    await getPCDepartments()
})


onUnmounted(() => {
    if (unsubscribePCStoreAction){
        unsubscribePCStoreAction()
    }
})

</script>