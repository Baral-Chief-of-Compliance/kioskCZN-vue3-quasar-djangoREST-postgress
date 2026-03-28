<template>
    <q-page>
        <titel-page 
            :path-name="INFO"
            titel="О кадровом центре"
        />
        <loading-spinner v-if="loading" :height="loadingHeight" />

        <div v-else-if="!loading && pcInfoStore.id" class="col q-mt-xl q-mx-xl">
            <q-tabs
                v-model="tab"
                class="text-grey"
                active-color="indigo"
                indicator-color="indigo"
                align="justify"
            >
                <q-tab :name="HEAD_INFO_PAGE" label="Руководство" />
                <q-tab :name="PC_INFO_PAGE" label="Контактная информация" />
                <q-tab :name="SOCIAL_NETWORK_PAGE" label="Социальные сети" />
            </q-tabs>

            <q-separator />

            <q-tab-panels v-model="tab" animated class="bg-grey-1">
                <q-tab-panel :name="HEAD_INFO_PAGE">
                    <head-info
                        :head-info="pcInfoStore.headInfo"
                    />
                </q-tab-panel>

                <q-tab-panel :name="PC_INFO_PAGE">
                    <contact-info 
                        :address="pcInfoStore.address"
                        :phones="pcInfoStore.phones"
                        :emails="pcInfoStore.emails"
                        :sites="pcInfoStore.sites"
                        :time-tables="pcInfoStore.timeTables"
                        :parent-org="pcInfoStore.parentOrg"
                    />
                </q-tab-panel>

                <q-tab-panel :name="SOCIAL_NETWORK_PAGE">
                    <social-netrwork-info 
                        :social-networks="pcInfoStore.socialNetworks"
                    />
                </q-tab-panel>

            </q-tab-panels>

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
import ContactInfo from 'src/components/infoAboutPC/ContactInfo.vue';
import NotFoundContent from 'src/components/NotFoundContent.vue';
import LoadingSpinner from 'src/components/LoadingSpinner.vue';
import { usePCStore } from 'src/stores/personalCenter';
import { usePCInfoStore, HEAD_INFO_PAGE, PC_INFO_PAGE, SOCIAL_NETWORK_PAGE } from 'src/stores/personalCenterInfo';
import { getPersonalCenterInfo } from 'src/axios/personalCenter';
import SocialNetrworkInfo from 'src/components/infoAboutPC/SocialNetrworkInfo.vue';

const pcInfoStore = usePCInfoStore()
const pcStore = usePCStore()


const loading = ref(true)

const tab = ref(HEAD_INFO_PAGE)


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

        console.log(res.data)

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