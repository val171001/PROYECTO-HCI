<template>
    <div class="q-pa-md row items-start q-gutter-md">
        <q-card v-for="code in codes" v-bind:key="code.codigo">
            <q-card-section>
                <div class="text-h6">{{code.marca}}</div>
            </q-card-section>
            <q-card-section>
                <div class="text-h8">¡Unicamente mayor a {{code.valorenpuntos}} puntos por usuario, para canjear!</div>
            </q-card-section>
            <q-card-section>
                <use-code :userid="user" :code="code.codigo" :marca="code.marca" :able="ableToBuy(code.valorenpuntos)" @buy="refresh"/>
            </q-card-section>
        </q-card>
        <q-page-sticky position="bottom-right" :offset="[18, 18]">
            <q-btn fab icon="arrow_back" color="primary" @click="main"/>
        </q-page-sticky>
    </div>
</template>

<script>
import router from '@/router'
import UseCode from '@/components/UseCode'
export default {
    name: 'Codes',
    components: {
        UseCode
    },
    data() {
        return {
            user: this.$user.id,
            points: 0,
            codes: []
        }
    },
    mounted () {
        this.refresh()
    },
    methods: {
        async getCodes() {
            this.$q.loading.show({ delay: 400 })
            const get = this.$http.get
            await get(
                '/client/codes'
            ).then( response => {

                this.codes = response.data
            }).catch(error => {
                console.log(error)
            })
            this.$q.loading.hide()
        },
        async getPoints() {
            this.$q.loading.show({ delay: 400 })
            const get = this.$http.get
            const email = this.$user.email

            await get(
                '/client/user/points',
                {
                    params: {
                        email: email
                    }
                }
            ).then(results => {
                this.points = results.data[0].puntos
            }).catch(error => {
                console.log(error)
            })
            this.$q.loading.hide()
        },
        ableToBuy(price){
            var able =  this.points > (price+1)
            console.log(able)
            return able
        },
        refresh(){
            this.getCodes()
            this.getPoints()
        },
        main() {
            router.push({name: 'Home'})
        }
    }
}
</script>
