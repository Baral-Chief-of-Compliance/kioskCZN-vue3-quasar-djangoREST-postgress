<template>
    <q-page>
        <titel-page titel="Игры" />
        <loading-spinner 
            v-if="loading" 
            :height="`${windowHeight}px`"
        />
        <div 
            v-else-if="!loading && games.length > 0"
            class="row justify-between q-mx-md"
        >
            <card-menu 
                v-for="g in games"
                :key="g.id"
                :titel="g.name"
                icon="sports_esports"
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
import CardMenu from 'src/components/CardMenu.vue';
import { getGames } from 'src/axios/games';


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