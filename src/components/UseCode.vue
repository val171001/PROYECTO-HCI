<template>
  <div class="q-pa-md">
    <q-item clickable tag="a" target="_blank" href="https://play.google.com/store/apps?hl=es">
      <q-item-section avatar>
        <q-icon name="img:https://elandroidelibre.elespanol.com/wp-content/uploads/2017/05/nuevo-icono-google-play-escritorio-1.jpg" />
      </q-item-section>
      <q-item-section>
        <q-item-label caption>Play Store</q-item-label>
      </q-item-section>
    </q-item>

     <div class="row no-wrap q-pa-md">
       <div class="column">
         <div class="text-h6 q-mb-md">Canjear los Puntos</div>
       </div>
       <q-separator vertical inset class="q-mx-lg" />

       <div class="column items-center">
          <q-btn
            label="Comprar"
            color='primary'
            size='l'
            @click="buy"
          />
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
    props: ["userid", "code"],
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
