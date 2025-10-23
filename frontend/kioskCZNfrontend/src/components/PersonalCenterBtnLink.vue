<template>
    <q-btn
        class="q-mb-sm base-btn-link"
        size="lg"
        style="min-width: 500px;"
        @click="goToPersonalCenterIndexPage"
        :label="props.label"
        color="indigo"
        unelevated
    ></q-btn>
</template>


<script setup>
import { useRouter } from 'vue-router';
import { INDEX } from 'src/router/pathName';

const router = useRouter()


function goToPersonalCenterIndexPage(){
    router.push({ name: INDEX, params: {pc: props.urlParam} })
}

const props = defineProps({
    label: {
        type: String,
        default: 'Наименование КЦ'
    },

    urlParam: {
        type: String,
        default: 'test'
    }
})

</script>

<style scoped>
    .base-btn-link{
        border-radius: 10px !important;
    }
</style>