<template>
    <q-page>
        <titel-page 
            :path-name="INFO"
            titel="Документы"
        />
        <loading-spinner v-if="loading" :height="loadingHeight" />

        <div v-else-if="!loading && documentsStore.documents.length > 0" class="row q-mt-lg q-mx-md">
            <div class="col-4">
                <scroll-area
                    :height="documentsListHeight"
                >
                    <service-card
                        class="q-mr-xl"
                        v-for="(doc, index) in documentsStore.getDocuments"
                        v-bind:key="doc.id"
                        :titel="doc.name"
                        :active="index === documentsStore.activeDocumentIndex"
                        @click-card="choseDocument(index)"
                    />
                </scroll-area>
            </div>

            <div class="col-8">
                <service-name
                    for-document
                    :label="documentsStore.getActiveDocumentName"
                    class="q-mb-sm"
                    v-model="documentNameHeight"
                />

                <scroll-area
                    :height="documentsViewHeight"
                    v-show="!documentLoading"
                >
                    <vue-pdf-embed 
                        @loaded="handelLoadedDocument"
                        :source="documentsStore.getDocumentFromActiveDocument" 
                    />
                </scroll-area>

                <loading-spinner v-show="documentLoading" :height="documentsViewHeight" />
            </div>
        </div>

        <not-found-content v-else :height="loadingHeight" />
    </q-page>
</template>

<script setup>
import { onMounted, onUnmounted, ref, inject, computed } from 'vue';
import { useWindowSize} from '@vueuse/core';
import VuePdfEmbed from 'vue-pdf-embed'

import { usePCStore } from 'src/stores/personalCenter';
import { useDocuments } from 'src/stores/documents';
import { getDocuments } from 'src/axios/documents';
import { INFO } from 'src/router/pathName';
import TitelPage from 'src/components/TitelPage.vue';
import NotFoundContent from 'src/components/NotFoundContent.vue';
import LoadingSpinner from 'src/components/LoadingSpinner.vue';
import ScrollArea from 'src/components/ScrollArea.vue';
import ServiceCard from 'src/components/ServiceCard.vue';
import ServiceName from 'src/components/ServiceName.vue';


const documentsStore = useDocuments()
const pcStore = usePCStore()

const loading = ref(true)
const documentLoading = ref(true)

const headerHeight = inject('headerHeight')
const {height: windowHeight } = useWindowSize()

const documentNameHeight = ref(0)

const loadingHeight = computed(() => {
    return  `${windowHeight.value - headerHeight.value}px`
})

const documentsListHeight = computed(() => {
    return  `${windowHeight.value - (headerHeight.value + 100)}px`
})

const documentsViewHeight = computed(() => {
    return  `${windowHeight.value - (headerHeight.value + documentNameHeight.value + 110)}px`
})

//Получить документы кадрового центра
const getPCDocuments = async() => {
    loading.value = true
    const res = await getDocuments()

    if (res.status != 200){
            return;
    }
    documentsStore.setStore(res.data)
    loading.value = false
}

//Обработка загрузки документа
const handelLoadedDocument = () => {
    documentLoading.value = false
}


// выбор кативного документа
const choseDocument = async (index) => {
    documentLoading.value = true
    documentsStore.setActiveDocument(index)
}

let unsubscribePCStoreAction = pcStore.$onAction(
    ({name, after }) => {
        after(async() => {
            if (name === 'setStore'){
                await getPCDocuments()
            }
        })
    }
)

onMounted(async () => {
    await getPCDocuments()
})

onUnmounted(() => {
    if (unsubscribePCStoreAction){
        unsubscribePCStoreAction()
    }
})
</script>