<template>
    <div>
        <div class="q-pa-md row items-start q-gutter-md">
            <q-card>
                <q-card-section>
                    <span> BIENVENIDO {{name}} </span>
                </q-card-section>
            </q-card>
            <q-card>
                <q-card-section>
                    <div class="text-h6">PUNTOS DISPONIBLES</div>
                </q-card-section>
                <q-card-section>
                    <div class="text-h6 flex flex-center">{{points}}</div>
                </q-card-section>
            </q-card>
            <q-btn label="Redimir puntos" @click="usePoints"/>
            <q-btn label="Ver mis códigos" @click="usedPoints"/>
            <q-btn label="Scan código" @click="ScanCode"/>
        </div>
    </div>
</template>

<script>
import router from '@/router'
export default {
    name: 'Main',
    data() {
        return {
            name: this.$user.name,
            points: 0
        }
    },
    mounted() {
        this.getPoints()
    },
    methods: {
        async getPoints() {
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
        },
        usePoints(){
            router.push({name: 'AvailableCodes'})
        },
        usedPoints(){
            router.push({name: 'UsedCodes'})
        },
        ScanCode(){
            router.push({name: 'ScanCode'})
        }
    }
}
</script>
