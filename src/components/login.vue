<template>
  <div class="fixed-center">
        <form action="a" @submit.prevent='login'>
        <q-card style="min-width: 300px">
            <q-img
              src="data:image/png;base64,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"
              :ratio="4/3"
            />
        </q-card>
        <q-card style="min-width: 300px">
            <q-card-section>
                <div class="q-pa-md flex flex-center text-h6">Iniciar Sesion</div>
            </q-card-section>
            <q-card-section class="q-gutter-xl">
                <q-form @submit="login">
                    <q-input
                        label="Nombre de usuario"
                        v-model="username"
                        :rules="[val => val !== null && val !== '' || 'Por favor ingrese nombre de usuario.']"
                    />
                    <q-input
                        label="Contraseña"
                        v-model="password"
                        type="password"
                        :rules="[val => val !== null && val !== '' || 'Por favor ingrese contraseña.']"
                    />
                    <div class="q-pa-md flex flex-center">
                      <div class="q-pa-sm">
                        <q-btn type="submit" label="Iniciar sesion"/>
                      </div>
                      <div class="q-pa-sm">
                        <q-btn label='Registrarse' @click="register"/>
                      </div>
                    </div>
                </q-form>
            </q-card-section>
        </q-card>
        </form>
    </div>
</template>

<style>
</style>

<script>
import router from '@/router'
export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: '',
      response: [],
    }
  },
  methods: {
    async login() {
      this.$q.loading.show({ delay: 400 })
      const email = this.username
      const password = this.password
      const post = this.$http.post

      await post(
        '/client/login',
        {
          email: email,
          password: password
        }
      ).then(results => {
        this.response = results.data
      }).catch(error => {
        console.log(error)
      })

      if(this.response.length > 0){
        this.$user.id = this.response[0].usuarioid
        this.$user.name = this.response[0].nombrecompleto
        this.$user.email = this.response[0].email
        this.$user.age = this.response[0].edad
        router.push({name: 'Home'})

      } else {
        console.log('User not found!')
      }
      this.$q.loading.hide()
    },
    register() {
      router.push({name: 'Register'})
    }
  }
  }
</script>
