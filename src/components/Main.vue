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

            <q-btn outline style="color: goldenrod;" label="REDIMIR PUNTOS" @click="usePoints"/>
            <q-btn outline style="color: goldenrod;" label="VER MIS CODIGOS" @click="usedPoints"/>
            <q-btn outline style="color: goldenrod;" label="ESCANEAR CODIGO" @click="ScanCode"/>
            <q-btn color="deep-orange" glossy label="CERRAR SESION" @click="login"/>

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
        },
        login(){
          router.push({name: 'LogIn'})
        }
    }
}
</script>
