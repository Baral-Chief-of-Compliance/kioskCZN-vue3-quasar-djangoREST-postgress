<template>
    <q-card 
        @click="goPage"
        class="q-mx-md q-my-xl no-shadow menu-card text-white text-left"
        :class="setColor"
        :style="{
            width: width + 'px',
            height: height + 'px'
        }"
    >
        <q-card-section>
            <div class="menu-card-titel q-mt-md q-ml-sm">{{ titel }}</div>
        </q-card-section>

        <q-card-actions>
            <q-icon class="menu-card-icon" :name="icon" :size="sizeIcon +'px'"></q-icon>
        </q-card-actions>
    </q-card>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';

const listOfColor = ['indigo-9', 'blue', 'orange-8']
const color = ref('')

const router = useRouter()

function getRandomInt(max){
    return Math.floor(Math.random() * max)
}

const props = defineProps({
    titel: {
        type: String,
        default: 'Наименование пункта'
    },
    icon: {
        type: String,
        default: 'today'
    },
    link: {
        type: String,
        default: 'index'
    },
    width: {
        type: Number,
        default: 400
    },
    height: {
        type: Number,
        default: 300
    },
    sizeIcon: {
        type: Number,
        default: 60
    }
})

onMounted(() => {
    color.value = listOfColor[getRandomInt(3)]
})

const setColor = computed(() => {
    return `bg-${color.value}`
})

function goPage(){
    router.push({name: props.link})
}

</script>

<style scoped>
    .menu-card{
        border-radius: 10px !important;
    }
    .menu-card-titel{
        font-size: 32px;
        font-weight: 700;

    }

    .menu-card-icon{
        position: absolute;
        bottom: 40px;
        right: 40px;
    }
</style>