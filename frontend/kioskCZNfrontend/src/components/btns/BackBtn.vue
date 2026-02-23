<template>
    <q-btn
        class="back-btn q-px-lg q-py-sm absolute-top-left q-ml-md"
        size="lg"
        label="Назад"
        @click="goHome"
        unelevated
        color="orange"
    >
    </q-btn>
</template>

<script setup>
import { useRouter } from 'vue-router';

import { usePCStore } from 'src/stores/personalCenter';
import { INDEX, CHOOSE_PC } from 'src/router/pathName';


const pcStore = usePCStore()
const router = useRouter()

const props = defineProps({
    pathName: {
        type: String,
        default: INDEX
    }
})

function goHome(){
    if (pcStore.getUrlParam != null){
        router.push({name: props.pathName, params: {pc: pcStore.getUrlParam}})
    }else{
        router.push({name: CHOOSE_PC})
    }
}

</script>


<style scoped>
    .back-btn{
        border-radius: 10px !important;
    }
</style>