<template>
    <div>
        <loading-spinner :height="props.width" v-if="!qrCodeValue" />
        <img 
            v-else :src="qrCodeValue"
            :alt="props.url"
            :style="qrCodeStyle"
        >
    </div>
</template>

<script setup>
import { ref,onMounted, computed } from 'vue';

import QRCode from 'qrcode';

import LoadingSpinner from '../LoadingSpinner.vue';

const qrCodeValue = ref(null)

const qrCodeStyle = computed(() => ({
    width: props.width,
    height: props.width
}))

const props = defineProps({
    url: {
        type: String,
        default: 'https://trudvsem.ru/'
    },
    width: {
        type: String,
        default: '300px'
    }
})



const generateQR = async url => {
  try {
    return await QRCode.toDataURL(url)
  } catch (err) {
    console.error(err)
  }
}

onMounted(async() => {
    qrCodeValue.value = await generateQR(props.url)

})

</script>