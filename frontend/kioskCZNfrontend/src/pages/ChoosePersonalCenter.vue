<template>
  <q-page class="flex flex-center">
    <div class="column">
        <personal-center-btn-link
            v-for="pc in personalCentersList"
            v-bind:key="pc.pc_query_param"
            :label="pc.pc_name"
            :url-param="pc.pc_query_param"
        />
    </div>
    </q-page>
</template>

<script setup>
import { onMounted, ref } from 'vue';

import PersonalCenterBtnLink from 'src/components/PersonalCenterBtnLink.vue';
import { getALLPersonalCenters } from 'src/axios/personalCenter';

const personalCentersList = ref([])

onMounted(async () =>{
    personalCentersList.value = await getALLPersonalCenters()
})

</script>