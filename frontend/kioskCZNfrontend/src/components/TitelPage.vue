<template>
    <div class="row q-mx-md q-mt-md">
        <back-btn />
        <div class="titel-page q-mx-auto text-indigo">{{ props.titel }}</div>
    </div>
</template>

<script setup>
import BackBtn from './btns/BackBtn.vue';

const props = defineProps({
    titel: {
        type: String,
        default: 'Наименование страницы'
    }
})

</script>

<style scoped>
    .titel-page{
        font-weight: 700;
        font-size: 30px;
    }

</style>