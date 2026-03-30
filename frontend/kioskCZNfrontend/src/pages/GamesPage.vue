<template>
    <q-page>
        <titel-page titel="Игры" />
        <loading-spinner 
            v-if="loading" 
            :height="`${windowHeight}px`"
        />
        <div 
            v-else-if="!loading && games.length > 0"
            class="q-col-gutter-md row items-start q-mx-md q-mt-xl"
        >
            <game-card 
                v-for="g in games"
                v-bind:key="g.id"
                :name="g.name"
                :img-url="g.img"
                :game-id="g.id"
            />
        </div>
        <not-found-content v-else :height="`${windowHeight}px`" />
    </q-page>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import TitelPage from 'src/components/TitelPage.vue';
import NotFoundContent from 'src/components/NotFoundContent.vue';
import LoadingSpinner from 'src/components/LoadingSpinner.vue';
import { useWindowSize } from '@vueuse/core';
import { usePCStore } from 'src/stores/personalCenter';
import { getGames } from 'src/axios/games';
import GameCard from 'src/components/games/GameCard.vue';


const pcStore = usePCStore()

const games = ref([])
const loading = ref(true)
const {height: windowHeight } = useWindowSize()


const getGamesFromBack = async () =>{
    loading.value = true
    const res = await getGames(pcStore.pcId)

    if (res.status !== 200){
        return;
    }

    games.value = res.data
    loading.value = false
}

onMounted(async () => {
    await getGamesFromBack()
})
</script>