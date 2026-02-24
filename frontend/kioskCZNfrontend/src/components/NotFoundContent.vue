<template>
    <div 
        class="flex flex-center"
        :style="{
            height: props.height
        }"
    >
        <div class="text-center text-blue text-h2 text-bold">
            На данный момент, тут нет контента...
        </div>
    </div>
</template>

<script setup>

const props = defineProps({
    height: {
        type: String,
        default: '400px'
    }
})

</script>