<template>
    <q-page>
        <titel-page 
            :path-name="VACANCIES"
            :title="districtsStore.getName"
        />
    </q-page>
</template>

<script setup>
import TitelPage from 'src/components/TitelPage.vue';
import LoadingSpinner from 'src/components/LoadingSpinner.vue';
import { useDistircts } from 'src/stores/districts';
import { VACANCIES } from 'src/router/pathName';
import { getDistrictDetail } from 'src/axios/districts';
import { usePCStore } from 'src/stores/personalCenter';


const districtsStore = useDistircts()


const getVacansyFromDistrict = async() => {
    
}

</script>