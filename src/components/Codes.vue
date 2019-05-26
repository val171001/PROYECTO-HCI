<template>
    <div class="q-pa-md row items-start q-gutter-md">
        <q-card v-for="code in codes" v-bind:key="code.codigo">
            <q-card-section>
                <div class="text-h6">{{code.marca}}</div>
            </q-card-section>
            <q-card-section>
                <div class="text-h8">Por solo {{code.valorenpuntos}} puntos usuario</div>
            </q-card-section>
            <q-card-section>
                <use-code :userid="user" :code="code.codigo"/>
            </q-card-section>
        </q-card>
    </div>
</template>

<script>
import UseCode from '@/components/UseCode'
export default {
    name: 'Codes',
    components: {
        UseCode
    },
    data() {
        return {
            user: this.$user.id,
            codes: []
        }
    },
    mounted () {
        this.getCodes()
    },
    methods: {
        async getCodes() {
            const get = this.$http.get
            await get(
                '/client/codes'
            ).then( response => {

                this.codes = response.data
            }).catch(error => {
                console.log(error)
            })
        }
    }
}
</script>
