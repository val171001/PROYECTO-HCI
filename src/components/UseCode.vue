<template>
  <div class="q-pa-md">
    <q-item v-if="marca === 'Google Play'"  clickable tag="a" target="_blank" href="https://play.google.com/store/apps?hl=es">
      <q-item-section avatar>
        <q-icon name="img:https://elandroidelibre.elespanol.com/wp-content/uploads/2017/05/nuevo-icono-google-play-escritorio-1.jpg" />
      </q-item-section>
      <q-item-section>
        <q-item-label caption>Play Store</q-item-label>
      </q-item-section>
    </q-item>

    <q-item v-else-if="marca === 'Steam'"  clickable tag="a" target="_blank" href="steampowered.com">
      <q-item-section avatar>
        <q-icon name="img:https://cdn.pixabay.com/photo/2018/05/08/21/29/steam-3384020_960_720.png" />
      </q-item-section>
      <q-item-section>
        <q-item-label caption>Steam</q-item-label>
      </q-item-section>
    </q-item>

    <q-item v-else-if="marca === 'Claro'"  clickable tag="a" target="_blank" href="steampowered.com">
      <q-item-section avatar>
        <q-icon name="img:https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Claro.svg/245px-Claro.svg.png" />
      </q-item-section>
      <q-item-section>
        <q-item-label caption>Claro</q-item-label>
      </q-item-section>
    </q-item>

     <div class="row no-wrap q-pa-md">
       <div class="column">
         <div class="text-h6 q-mb-md">Canjear los Puntos</div>
       </div>
       <q-separator vertical inset class="q-mx-lg" />

       <div class="column items-center">
          <q-btn
            v-if="buy"
            label="Comprar"
            color='positive'
            size='l'
            @click="buy"
          />
          <span v-else>Necesitas mas puntos.</span>

       </div>
     </div>
 </div>
 
<!--
 <div>
     <q-btn label="Comprar" @click="buy"/>
 </div>
 -->
</template>

<script>
export default {
    name: 'UsePoints',
    props: ["userid", "code", "marca", "buy"],
    methods: {
        async buy(){
            console.log(this.userid, this.code)
            const post = this.$http.post
            await post(
                '/client/user/get/code',
                {
                    userId: this.userid,
                    code: this.code
                }
            ).then(results => {
                console.log(results)
            }).catch(error => {
                console.log(error)
            })
        }
    }
}
</script>
