<template>
    <div @click="useSearchingField" ref="searchField" class="col">
        <div :class="searchFieldClass">
            <div class="col-auto q-mr-md">
                <q-icon 
                    name="search" 
                    size="30px"
                    color="grey-7"
                />
            </div>
            <div :class="searchValueClass">
                {{ searchValue }}
            </div>
        </div>
    </div>
</template>

<script setup>
import { computed, ref, useTemplateRef, watch } from 'vue';
import { useElementSize } from '@vueuse/core';


const active = ref(false)
const searchValue = ref('Найти...')

const searchField = useTemplateRef('searchField')
const { height: searchFieldHeight } = useElementSize(searchField)

const model = defineModel(0)


const searchFieldClass = computed(() => ({
    'row': true,
    'search-input': true,
    'active soft-glow': active.value,
    'inactive': !active.value,
}))

const searchValueClass = computed(() => ({
    'col-11 justify-start content-center flex search-text': true,
    'st-active': active.value,
    'st-inactive text-grey': !active.value,
}))

watch(searchFieldHeight, (newValue) => {
    model.value = newValue
})

const useSearchingField = () => {
    active.value = !active.value
    if (active.value){
        searchValue.value = ''
    }else{
        searchValue.value = 'Найти...'
    }
}
</script>

<style scoped>
    .search-input{
        border-radius: 15px;
        padding: 20px;
    }

    .active{
        border: 4px solid var(--q-indigo);
    }

    .inactive{
        border: 4px solid var(--q-blue-4);
    }

    .soft-glow {
        background: #fff;
        box-shadow: 0 0 20px 10px rgba(0, 0, 0, 0.1);
        border-radius: 12px;
        padding: 20px;
    }

    .search-text{
        font-size: 16px;
    }

    .st-active {
        font-weight: 500;
        color: var(--q-dark);
    }

    .st-inactive {
        font-weight: 400;
    }
</style>