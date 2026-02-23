<template>
    <div class="flex flex-center" :style="{
        height: props.height
    }">
        <div class="q-gutter-md row items-center">
        <q-spinner-cube
            size="5.5em"
            color="orange"
        />
        </div>
  </div>
</template>

<script setup>

const props = defineProps({
    height:{
        type: String,
        default: '400px'
    }
})
</script>