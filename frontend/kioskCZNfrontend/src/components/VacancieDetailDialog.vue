<template>
    <q-dialog 
        ref="dialogRef" @hide="onDialogHide"
        :maximized="false"
        :style="{ maxWidth: 'none' }"
>
        <q-card :style="cardStyle">   
            <q-card-section>
                {{ props.vacancieId }}
            </q-card-section>
            <q-card-section>
                <loading-spinner 
                    v-if="loading"
                    :height="loadingHeight" 
                />
                <scroll-area
                    :height="loadingHeight" 
                >

                </scroll-area>
            </q-card-section>
            <q-separator></q-separator>
            <q-card-actions>
                <q-btn 
                    class="full-width cancel-btn" 
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

const { dialogRef, onDialogHide, onDialogCancel } = useDialogPluginComponent()
const loading = ref(true)

const {height: windowHeight, width: windowWidth} = useWindowSize()

const loadingHeight = computed(() => {
    return `${windowHeight.value * 0.66}px`
})

const cardStyle = computed(() => ({
    width : `${windowWidth.value * 0.7}px`,
    maxWidth: '90vw',
    height: '81vh'
}))


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
</style>