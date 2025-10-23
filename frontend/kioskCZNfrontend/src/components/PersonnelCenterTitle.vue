<template>
    <div class="pc-titel text-indigo">
        {{ pcTitle }}
    </div>
</template>

<script setup>
import { computed } from 'vue';

import { usePCStore } from 'src/stores/personalCenter';

const psStore = usePCStore()

const pcTitle = computed(() => {
    return psStore.getPCName === null ? "Наименование Кадрового Центра" : `${psStore.getPCName} кадровый центр`
})


defineProps({
    title: {
        type: String,
        default: "Наименование Кадрового Центра"
    }
})

</script>

<style scoped>
    .pc-titel{
        font-weight: 700;
        font-size: 40px;
    }
</style>