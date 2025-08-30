<template>
    <div class="date-time text-indigo text-center q-mr-xl">
        <div>{{ getHourMinuteSeconds(date) }}</div>
        <div>{{ getDayMonthYear(date) }}</div>
    </div>
</template>


<script setup>
import { onMounted, ref, onUnmounted } from 'vue';

const date = ref(0)
const intervalId = ref('')

onMounted(()=>{
    date.value = Date.now()
    intervalId.value = setInterval(() => date.value = Date.now(), 1000);
})

onUnmounted(()=>{
    if (intervalId.value) clearInterval(intervalId.value)
})

//функция для преобразования секунд в дату
function getDayMonthYear(seconds){
    var date = new Date(seconds)
    var day = date.getDate()
    var month = date.getMonth()

    if (day / 10  < 1) day = `0${day}`
    if (month / 10 < 1) month = `0${month}` 
    return `${day}.${month}.${date.getFullYear()}`
}

//функция для преобразования секунд во время
function getHourMinuteSeconds(secondsUnix){
    var time = new Date(secondsUnix)
    var hours = time.getHours()
    var minutes = time.getMinutes()
    var seconds = time.getSeconds()

    if (hours / 10 < 1) hours = `0${hours}`
    if (minutes / 10 < 1) minutes = `0${minutes}`
    if (seconds / 10 < 1) seconds = `0${seconds}`

    return `${hours}:${minutes}:${seconds}`

}

</script>

<style scoped>
    .date-time{
        letter-spacing: 2px;
        font-size: 20px;
        font-weight: 500;
        line-height: 25px;
    }
</style>