<template>
    <div class="row q-mx-md q-mt-md">
        <back-btn 
            :path-name="props.pathName"
        />
        <div class="titel-page q-mx-auto text-indigo">{{ props.titel }}</div>
    </div>
</template>

<script setup>
import BackBtn from './btns/BackBtn.vue';
import { INDEX } from 'src/router/pathName';


const props = defineProps({
    titel: {
        type: String,
        default: 'Наименование страницы'
    },
    pathName: {
        type: String,
        default: INDEX
    }
})

</script>

<style scoped>
    .titel-page{
        font-weight: 700;
        font-size: 30px;
    }

</style>