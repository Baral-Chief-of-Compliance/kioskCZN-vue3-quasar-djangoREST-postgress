<template>
    <div class="row">
        <div class="col">
            <q-img 
                v-if="props.img"
                :src="props.img"
                fit="cover"
                style="height: 500px; max-width: 400px"
            />

            <q-img v-else
                src="/headInfoPC/boss.png"
                style="height: 500px; max-width: 400px"
            />
        </div>
        <div class="col">
            <div class="text-indigo text-h5 text-bold">{{ props.fio }}</div>

            <div class="text-blue text-h5 q-mt-md">{{ props.name }}</div>

            <div class="text-indigo text-h5 q-mt-xl">Телефон:</div>
            <div class="text-blue text-h5 text-bold"
                v-for="(p, index) in props.phones"
                v-bind:key="index"
            >
                {{ p.phone }}
            </div>

            <div class="text-indigo text-h5 q-mt-xl">Электронная почта:</div>
            <div class="text-blue text-h5 text-bold"
                v-for="(e, index) in props.emails"
                v-bind:key="index"
            >
                {{ e.email }}
            </div>

            <div class="text-indigo text-h5 q-mt-xl">Часы приема:</div>
            <div class="text-blue text-h5 text-bold"
                v-for="(t, index) in props.timeTable"
                v-bind:key="index"
            >
                {{defineDayOfWeek(t.day_of_week)}} : {{ showTime(t.start_time, t.end_time)}}
            </div>
        </div>
    </div>
</template>

<script setup>

const defineDayOfWeek = (dayOfWeek) => {
    if (dayOfWeek === 0){
        return 'Пн'
    }else if (dayOfWeek === 1){
        return 'Вт'
    }else if (dayOfWeek === 2){
        return 'Ср'
    }else if (dayOfWeek === 3){
        return 'Чт'
    } else if (dayOfWeek === 4){
        return 'Пт'
    } else if (dayOfWeek === 5){
        return 'Сб'
    } else if (dayOfWeek === 6){
        return 'Вс'
    }
}

const showTime = (startTime, endTime) => {
    const formatTime = (time) => {
        // Берем только часы и минуты (первые 5 символов)
        return time.substring(0, 5);
    };
    return `с ${formatTime(startTime)} по ${formatTime(endTime)}`;
}

const props = defineProps(
    {
        img: {
            type: String,
            default: null
        },

        fio: {
            type: String,
            default: 'ФИО Директора'
        },

        name: {
            type: String,
            default: 'Наименование поста'
        },

        phones: {
            type: Array,
            default: () => []
        },

        emails: {
            type: Array,
            default: () => []
        },

        timeTable: {
            type: Array,
            default: () => []
        }


    }
)
</script>