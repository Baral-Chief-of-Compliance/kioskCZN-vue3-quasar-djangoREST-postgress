<template>
    <tab-titel 
        titel-first="Информация"
        titel-second="о социальных сетях и мессенджерах"
    />
    <div class="col q-mt-xl">
        <div class="text-h4 text-indigo info">
            Приглашаем подключиться к нашим группам<br>
            в социальной сети Вконтакте, воспользовавшись QR-кодами ниже.
        </div>
        <div :class="qrCodeRowClass" v-if="props.socialNetworks.length > 0">
            <div 
                class="col-1 q-mx-xl"
                v-for="sn in props.socialNetworks"
                v-bind:key="sn.id"
                style="width: 400px;"
            >
                <div 
                    style="width: 400px;" 
                    class="text-center text-h5 text-blue text-bold"
                >
                    {{ sn.name }}
                </div>
                <qr-code 
                    :url="sn.link"
                    width="400px"
                />
            </div>
        </div>

        <div class="text-h5 text-bold text-blue text-center q-mt-xl" v-else>
            Ой, не удалось найти ссылки на социальные сети, попробуйте позже...
        </div>
    </div>
</template>

<script setup>
import { computed } from 'vue';

import TabTitel from './TabTitel.vue';
import QrCode from '../vacancie/QrCode.vue';

const qrCodeRowClass = computed(() => ({
    'row flex q-mt-xl' : true,
    'justify-between' : props.socialNetworks.length > 1,
    'justify-center': props.socialNetworks.length == 1
}))

const props = defineProps({
    socialNetworks: {
        type: Array,
        default: () => []
    }
})
</script>

<style scoped>
.info{
    font-weight: 600;
}

</style>