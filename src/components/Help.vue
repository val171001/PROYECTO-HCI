<template>
    <div>
        <div v-for="faq in faqs" v-bind:key="faq.title" class="q-pa-md text-justify">
            <q-card>
                <q-card-section>
                    <div class="text-h6">{{faq.title}}</div>
                </q-card-section>
                <q-card-section>
                    <p>
                        {{faq.message}}
                    </p>
                </q-card-section>
            </q-card>
        </div>
        <q-page-sticky position="bottom-right" :offset="[18, 18]">
            <q-btn fab icon="arrow_back" color="primary" @click="main"/>
        </q-page-sticky>
    </div>
</template>

<script>
import router from '@/router'
export default {
    name: 'Help',
    data(){
        return {
            faqs: [{title: '¿Como funciona?: ',
                    message: 'Con esta aplicacion ud puede ganar puntos que puede usar para canjear por premios, para ganar puntos todo lo que usted tiene que hacer es ingresar la lata en una de nuestras maquinas esta le dara un codigo qr el cual ud escaneara usando esta misma app y asi ira acumulando puntos. '},
                    
                    {title:'Camera error:',
                    message:'Para que pueda ser utilizada esta app en movil se recomienda bastante utilizar el navegador Mozilla Firefox, ya que desde este ud podra escoger la camara que le sea mas util (trasera o delantera) ' },

                    {title:'Base de datos: ',
                    message:'Si por algun motivo presenta problemas con la base de datos revose su conexion a internet, cierre la aplicacion e intente de nuevo. '},

                    {title: 'Como se utiliza la maquina:',
                    message:'La maquina tiene un funcionamiento bastante sencillo. Solo hale levemente la tapadera y coloque la lata en la silueta designada, ahora empuje la tapadera y la lata caera, finalmente escanee el codigo QR que aparecer[a en pantalla con el  escaner incluido en esta aplicacion.'}]
                            }
    },
    methods: {
        main() {
            router.push({name: 'Home'})
        }
    }
}
</script>

