<template>
    <q-card 
        class="cab-info-card absolute-top-right text-center q-mr-xl"
    >
        <q-card-section>
            <div class="text-indigo text-h4 text-bold q-mb-md">{{ props.name }}</div>
            <div
                v-for="w in props.workers"
                v-bind:key="w.id"
                
            >
                <div class="text-h6 text-left row">
                    <span class="col">{{ w.fio }}</span>
                    <span class="col">
                        {{ w.post_name }}
                    </span>
                </div>
                <q-separator class="q-mb-md"></q-separator>
            </div>
            
        </q-card-section>
    </q-card>
</template>

<script setup>
    const props = defineProps({
        name: {
            type: String,
            default: 'Кабинет'
        },

        workers: {
            type: Array,
            default: () => []
        }
    })
</script>


<style scoped>
    .cab-info-card{
        border-radius: 10px !important;
        width: 600px;
    }
</style>