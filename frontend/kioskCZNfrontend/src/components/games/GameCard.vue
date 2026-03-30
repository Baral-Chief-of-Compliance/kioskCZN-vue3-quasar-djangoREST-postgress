<template>
    <div class="col-4" @click="goGame">
        <q-img
            class="game-card"
            :src="gameUrl"
        >
            <div class="absolute-bottom text-h3 text-center">
                {{ props.name }}
            </div>
        </q-img>
    </div>
</template>

<script setup>
import { computed } from 'vue';

import { useRouter } from 'vue-router';
import { GAMES_DETAIL } from 'src/router/pathName';

const router = useRouter()


const gameUrl = computed(() => {
    if (props.imgUrl){
        return props.imgUrl
    }else{
        return '/base_game_img.jpeg'
    }
})


const goGame = () => {
    router.push(
        {name: GAMES_DETAIL, params: {game_id: props.gameId}}
    )
}
const props = defineProps({
    name: {
        type: String,
        default: 'Наименование'
    },

    imgUrl: {
        type: String,
        default: '/base_game_img.jpeg'
    },

    gameId: {
        type: Number,
        default: 0
    }
})

</script>

<style scoped>

.game-card{
    border-radius: 10px !important;
    height: 400px;
}
</style>