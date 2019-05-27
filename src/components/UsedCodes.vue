<template>
    <div class="q-pa-md row items-start q-gutter-md">
        <q-card v-for="code in codes" v-bind:key="code.codigo">
          <q-card-section>
              <q-item-label caption> Marca: </q-item-label>
              <!--Si la marca es Google Play-->
              <q-item v-if="code.marca === 'Google Play'"  clickable tag="a" target="_blank" href="https://play.google.com/store/apps?hl=es">
                <q-item-section avatar>
                  <q-icon name="img:https://elandroidelibre.elespanol.com/wp-content/uploads/2017/05/nuevo-icono-google-play-escritorio-1.jpg" />
                </q-item-section>
                <q-item-section>
                  <q-item-label caption>{{code.marca}}</q-item-label>
                </q-item-section>
              </q-item>
              <!--Si la marca es steam-->
              <q-item v-else-if="code.marca === 'Steam'"  clickable tag="a" target="_blank" href="steampowered.com">
                <q-item-section avatar>
                  <q-icon name="img:https://cdn.pixabay.com/photo/2018/05/08/21/29/steam-3384020_960_720.png" />
                </q-item-section>
                <q-item-section>
                  <q-item-label caption>{{code.marca}}</q-item-label>
                </q-item-section>
              </q-item>
              <!-- Si la marca es claro-->
              <q-item v-else-if="code.marca === 'Claro'"  clickable tag="a" target="_blank" href="steampowered.com">
                <q-item-section avatar>
                  <q-icon name="img:https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Claro.svg/245px-Claro.svg.png" />
                </q-item-section>
                <q-item-section>
                  <q-item-label caption>{{code.marca}}</q-item-label>
                </q-item-section>
              </q-item>
          </q-card-section>
          <q-card-section>
              <q-item-label caption> Puntos Canjeados: </q-item-label>
              <q-item-label header>{{code.valorcodigo}}</q-item-label>
          </q-card-section>
            <q-card-section>
                <q-item-label caption> Codigo: </q-item-label>
                <q-item-label header>{{code.codigo}}</q-item-label>
            </q-card-section>
        </q-card>
        <div class="q-pa-md row items-start q-gutter-md">
          <q-btn label="Regresar" color='positive' @click="main"/>
        </div>
    </div>
</template>

<script>
import router from '@/router'
export default {
    name: 'UsedCodes',
    data() {
        return {
            codes: []
        }
    },
    mounted(){
        this.getCodes()
    },
    methods: {
        async getCodes(){
            const get = this.$http.get
            const id = this.$user.id
            await get(
                '/client/user/get/code/used',
                {
                    params: {
                        userId: id
                    }
                }
            ).then(res => {
                this.codes = res.data
            }).catch(error => {
                console.log(error)
            })
        },
        main() {
          router.push({name: 'Home'})
        }
    }
}
</script>
