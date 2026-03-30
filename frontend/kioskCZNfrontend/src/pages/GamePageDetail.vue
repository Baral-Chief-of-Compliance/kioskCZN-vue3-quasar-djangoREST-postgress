<template>
    <q-page>
        <titel-page 
            :titel="gameName" 
            :path-name="GAMES"
        />
        <loading-spinner 
            v-if="loading"
            :height="`${windowHeight}px`"
        />

        <iframe v-else-if="!loading && gameUrl !== null"
            :src="gameUrl"
            :width="windowWidht" 
            :height="heightGame"
            frameborder="0"
        >
        </iframe>

        <empty-block-info 
            v-else
            :height="windowHeight"
        />
    </q-page>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue';
import TitelPage from 'src/components/TitelPage.vue';
import { GAMES } from 'src/router/pathName';
import LoadingSpinner from 'src/components/LoadingSpinner.vue';
import { usePCStore } from 'src/stores/personalCenter';
import { useWindowSize } from '@vueuse/core';
import { getGameById } from 'src/axios/games';
import { useRoute } from 'vue-router';
import EmptyBlockInfo from 'src/components/EmptyBlockInfo.vue';

const {width: windowWidht, height: windowHeight } = useWindowSize()
const heightGame = computed(() => {
    return windowHeight.value - 100
})

const route = useRoute()

const gameName = ref('Наименование игры')
const loading = ref(true)

const gameUrl = ref(null)

const pcStore = usePCStore()

const getGame = async() => {
    loading.value = true

    if ('game_id' in route.params){
        const res = await getGameById(route.params.game_id)
        if (res.status !== 200){
            return;
        }

        gameName.value = res.data.name
        gameUrl.value = res.data.url
    }

    loading.value = false
}

let unsubscribePCStoreAction = pcStore.$onAction(
    ({name, after }) => {
        after(async() => {
            if (name === 'setStore'){
                await getGame()
            }
        })
    }
)


onMounted(async() => {
    await getGame()
})

onUnmounted(() => {
    unsubscribePCStoreAction()
})
</script>