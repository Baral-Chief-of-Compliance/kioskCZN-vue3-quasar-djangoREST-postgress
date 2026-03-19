<template>
    <q-dialog 
        ref="dialogRef" @hide="onDialogHide"
        :maximized="false"
        :style="{ maxWidth: 'none' }"
>
        <q-card :style="cardStyle">   
            <q-card-section>
                <div class="vacansy-name">{{ vacansyName }}</div>
            </q-card-section>
            <q-card-section>
                <loading-spinner 
                    v-if="loading"
                    :height="loadingHeight" 
                />
                <scroll-area
                    v-else
                    :height="loadingHeight" 
                >
                    <div v-if="vacancieInfo && Object.keys(vacancieInfo).length" class="col q-mx-xl">
                        <vacancie-row-info
                        v-for="([key, value], index) in objectEntries"
                        :key="index"
                        :titel="key"
                        :value="value"
                        />
                    </div>
                    
                    <vacancie-address-info class="q-mx-xl"
                        :width="widthForAddress"
                        :longitude="vacancieInfo['longitude']"
                        :latitude="vacancieInfo['latitude']"
                        :vacancy-address="vacancieInfo['vacancyAddress']"
                        :vacancy-address-additional-info="vacancieInfo['vacancyAddressAdditionalInfo']"
                    />

                    <vacanci-qr-codes 
                        class="q-mx-xl q-mt-xl"
                        :vacancy-url="vacancieInfo['vacancyUrl']"
                        :url="vacancieInfo['url']"
                    />
                </scroll-area>
            </q-card-section>
            <q-separator></q-separator>
            <q-card-actions class="justify-end">
                <q-btn 
                    class="cancel-btn" 
                    label="Закрыть" 
                    @click="onDialogCancel"
                    unelevated
                    color="blue"
                    size="lg"
                    no-caps
                />
            </q-card-actions>
        </q-card>

    </q-dialog>
</template>

<script setup>
import { useDialogPluginComponent } from 'quasar';
import { onMounted, ref, computed } from 'vue';

import { useWindowSize } from '@vueuse/core';

import LoadingSpinner from './LoadingSpinner.vue';
import ScrollArea from './ScrollArea.vue';
import { getVacancieDetail } from 'src/axios/vacancies';
import VacancieRowInfo from './vacancie/VacancieRowInfo.vue';
import VacancieAddressInfo from './vacancie/VacancieAddressInfo.vue';
import VacanciQrCodes from './vacancie/VacanciQrCodes.vue';

const { dialogRef, onDialogHide, onDialogCancel } = useDialogPluginComponent()
const loading = ref(true)

const vacancieInfo = ref({})

const vacansyName = computed(() => {
    if (vacancieInfo.value != {}){
        if ('vacancyName' in vacancieInfo.value){
            return vacancieInfo.value.vacancyName
        }
    }

    return 'Загрузка...'
})

const objectEntries = computed(() => {
  return Object.entries(vacancieInfo.value)
})

const {height: windowHeight, width: windowWidth} = useWindowSize()

const loadingHeight = computed(() => {
    return `${windowHeight.value * 0.66}px`
})

const cardStyle = computed(() => ({
    width : `${windowWidth.value * 0.7}px`,
    maxWidth: '90vw',
    height: '81vh'
}))

const widthForAddress = computed(() => {
    return `${windowWidth.value * 0.6}px`
})


defineEmits([
    ...useDialogPluginComponent.emits
])

const props = defineProps({
    vacancieId: {
        type: String
    }
})

const getVacancieDetailById = async () => {
    loading.value = true
    const res = await getVacancieDetail(props.vacancieId)

    if (res.status != 200){
        return;
    }
    vacancieInfo.value = res.data
    loading.value = false
}

onMounted(async() => {
    await getVacancieDetailById()
})

</script>

<style scoped>
    .cancel-btn{
        border-radius: 10px !important;
    }
    .vacansy-name{
        color: #25282b;
        font-size: 20px;
        line-height: 1.4;
        font-weight: 600;
        letter-spacing: .2px;
        word-break: break-word;
    }
</style>