<template>
    <q-page>
        <titel-page 
            :path-name="INFO"
            titel="О кадровом центре"
        />
        <loading-spinner v-if="loading" :height="loadingHeight" />

        <div v-else-if="!loading && pcInfoStore.id" class="col q-mt-xl q-mx-xl">
            <head-info v-if="pcInfoStore.activePage === HEAD_INFO_PAGE"
                :head-info="pcInfoStore.headInfo"
            />

            <q-btn 
                size="xl"
                unelevated
                rounded
                class="absolute-bottom-right q-mb-xl q-mr-xl"
            >
                <q-icon size="xl" name="arrow_right" color="orange" />
                <q-icon size="xl" name="arrow_right" color="orange" />
                <q-icon size="xl" name="arrow_right" color="orange" />
            </q-btn>
        </div>
        <not-found-content v-else :height="loadingHeight" />
    </q-page>
</template>

<script setup>
import { onMounted, onUnmounted, ref, inject, computed } from 'vue';
import { useWindowSize } from '@vueuse/core';

import { INFO } from 'src/router/pathName';
import TitelPage from 'src/components/TitelPage.vue';
import HeadInfo from 'src/components/infoAboutPC/HeadInfo.vue';
import NotFoundContent from 'src/components/NotFoundContent.vue';
import LoadingSpinner from 'src/components/LoadingSpinner.vue';
import { usePCStore } from 'src/stores/personalCenter';
import { usePCInfoStore, HEAD_INFO_PAGE } from 'src/stores/personalCenterInfo';
import { getPersonalCenterInfo } from 'src/axios/personalCenter';

const pcInfoStore = usePCInfoStore()
const pcStore = usePCStore()


const loading = ref(true)


const headerHeight = inject('headerHeight')
const {height: windowHeight } = useWindowSize()

const loadingHeight = computed(() => {
    return  `${windowHeight.value - headerHeight.value}px`
})

const getPCInfo = async () => {
    loading.value = true

    if (pcStore.pcId != null){
        const res = await getPersonalCenterInfo(pcStore.pcId)

        if (res.status != 200){
            return;
        }

        pcInfoStore.setStore(res.data)
    }

    loading.value = false
}


let unsubscribePCStoreAction = pcStore.$onAction(
    ({name, after }) => {
        after(async() => {
            if (name === 'setStore'){
                await getPCInfo()
            }
        })
    }
)

onMounted(async () => {
    pcInfoStore.$reset()
    await getPCInfo()
})


onUnmounted(() => {
    if (unsubscribePCStoreAction){
        unsubscribePCStoreAction()
    }
})
</script>