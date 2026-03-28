<template>
    <tab-titel 
        titel-first="Контактная информация"
    />

    <div class="row q-mt-xl">
        <div class="col-5">
            <titel-punkt-info 
                icon="explore"
                titel="Адрес"
            />

            <div class="q-mt-md" v-if="props.address.length > 0">
                <content-punkt-info  
                    v-for="(a, i) in props.address"
                    v-bind:key="i"
                    :content="a.address"
                />
            </div>
            <content-punkt-info class="q-mt-md" v-else  />

            <titel-punkt-info
                class="q-mt-xl"
                icon="call"
                titel="Телефоны"
            />

            <div class="q-mt-md" v-if="props.phones.length > 0">
                <content-punkt-info 
                    v-for="(p, i) in props.phones"
                    v-bind:key="i"
                    :content="phoneTitel(p.phone, p.name)"
                />
            </div>
            <content-punkt-info class="q-mt-md" v-else  />


            <titel-punkt-info
                class="q-mt-xl"
                icon="alternate_email"
                titel="Электронная почта"
            />


            <div class="q-mt-md" v-if="props.emails.length > 0">
                <content-punkt-info 
                    v-for="(e, i) in props.emails"
                    v-bind:key="i"
                    :content="emailTitel(e.email, e.name)"
                />
            </div>
            <content-punkt-info class="q-mt-md" v-else  />

            <titel-punkt-info
                class="q-mt-xl"
                icon="language"
                titel="Сайт"
            />

            <div class="q-mt-md" v-if="props.sites.length > 0">
                <content-punkt-info 
                    v-for="(s, i) in props.sites"
                    v-bind:key="i"
                    :content="siteTitel(s.url, s.name)"
                />
            </div>
            <content-punkt-info class="q-mt-md" v-else  />

            <div class="q-mt-sm" v-if="props.sites.length > 0">
                <qr-code
                    v-for="(s, i) in props.sites"
                    v-bind:key="i"
                    :url="s.url"
                    width="160px"
                />
            </div>

        </div>
        <div class="col">
            <titel-punkt-info 
                icon="calendar_month"
                titel="График работы"
            />

            <div class="q-my-md" v-if="props.timeTables.length > 0">
                <div class="row">
                    <div class="col">
                        <day-row-time-table
                            class="q-mb-sm"
                            v-for="(d, i) in props.timeTables.filter(item => !item.day_off)"
                            v-bind:key="i"
                            :day-of-week="d.day_of_week"
                            :day-off="d.day_off"
                            :time-start="d.time_start"
                            :time-end="d.time_end"
                        />
                    </div>
                    <div class="col">
                        <day-row-time-table 
                            class="q-mb-sm"
                            v-for="(d, i) in props.timeTables.filter(item => item.day_off)"
                            v-bind:key="i"
                            :day-of-week="d.day_of_week"
                            :day-off="d.day_off"
                            :time-start="d.time_start"
                            :time-end="d.time_end"
                        />
                    </div>
                </div>

            </div>
            <content-punkt-info class="q-mt-md" v-else  />

            <titel-punkt-info 
                icon="card_travel"
                titel="Вышестоящие организации"
            />

            <div v-if="props.parentOrg">
                <div class="text-h5 text-indigo q-my-md text-bold">{{ props.parentOrg.name }}</div>

                <!-- Адрес -->
                <div class="row q-mb-md">
                    <div class="text-h5 text-indigo col-3 pareng-org-info">Адрес</div>
                    <div 
                        v-if="props.parentOrg.address" 
                        class="col text-h5 text-blue"
                    >
                        <div
                            v-for="a in props.parentOrg.address"
                            v-bind:key="a.id"
                            class="pareng-org-info"
                        >
                            {{ a.address }}
                        </div>
                    </div>
                    <div v-else class="col text-h5 text-blue">Не указан</div>
                </div>

                <!-- Телефон -->
                <div class="row q-mb-md">
                    <div class="text-h5 text-indigo col-3 pareng-org-info">Телефон</div>
                    <div 
                        v-if="props.parentOrg.phones" 
                        class="col text-h5 text-blue"
                    >
                        <div
                            v-for="a in props.parentOrg.phones"
                            v-bind:key="a.id"
                            class="pareng-org-info"
                        >
                            {{ a.phone }}
                        </div>
                    </div>
                    <div v-else class="col text-h5 text-blue">Не указан</div>
                </div>


                <!-- Электронная почта -->
                <div class="row q-mb-md">
                    <div class="text-h5 text-indigo col-3 pareng-org-info">Электронная<br>почта</div>
                    <div 
                        v-if="props.parentOrg.emails" 
                        class="col text-h5 text-blue"
                    >
                        <div
                            v-for="a in props.parentOrg.emails"
                            v-bind:key="a.id"
                            class="pareng-org-info"
                        >
                            {{ a.email }}
                        </div>
                    </div>
                    <div v-else class="col text-h5 text-blue">Не указан</div>
                </div>
            </div>
            <content-punkt-info class="q-mt-md" v-else  />


        </div>
    </div>
</template>

<script setup>
import QrCode from '../vacancie/QrCode.vue';

import TabTitel from './TabTitel.vue';
import TitelPunktInfo from './TitelPunktInfo.vue';
import ContentPunktInfo from './ContentPunktInfo.vue';
import DayRowTimeTable from './DayRowTimeTable.vue';

const props = defineProps({
    address: {
        type: Array,
        default: () => []
    },

    phones: {
        type: Array,
        default: () => []
    },

    emails: {
        type: Array,
        default: () => []
    },

    sites: {
        type: Array,
        default: () => []
    },

    timeTables: {
        type: Array,
        default: () => []
    },

    parentOrg: {
        type: Object,
        default: null
    }
})

const phoneTitel = (phone, name) => {
    if (name !== null){
        return `${phone} - ${name}`
    }else{
        return phone
    }
}

const emailTitel = (email, name) => {
    if (name !== null){
        return `${email} - ${name}`
    }else{
        return email
    }
}

const siteTitel = (url, name) => {
    if (name !== null){
        return `${url} - ${name}`
    }else{
        return url
    }
}
</script>

<style scope>
.pareng-org-info {
    font-weight: 600;
}

</style>