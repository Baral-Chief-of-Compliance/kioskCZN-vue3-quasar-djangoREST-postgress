<template>
    <tab-titel 
        titel-first="Информация"
        titel-second="о руководстве учреждения"
    />

    <div class="row q-mt-xl">
        <div class="col">
            <head-card 
                :img="props.headInfo.main_head_photo"
                :fio="props.headInfo.main_head_worker"
                :name="props.headInfo.main_head_name"
                :phones="props.headInfo.main_head_phones"
                :emails="props.headInfo.main_head_emails"
                :time-table="props.headInfo.main_head_timetable"
            />
        </div>
        <div class="col">
            <head-card 
                :img="props.headInfo.head_photo"
                :fio="props.headInfo.head_worker"
                :name="props.headInfo.head_name"
                :phones="props.headInfo.head_phones"
                :emails="props.headInfo.head_emails"
                :time-table="props.headInfo.head_timetable"

            />
        </div>
    </div>
</template>

<script setup>
import HeadCard from './HeadCard.vue';
import TabTitel from './TabTitel.vue';

const props = defineProps({
    headInfo: {
        type: Object,
    }
})
</script>