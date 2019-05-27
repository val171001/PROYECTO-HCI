<template>
  <div class="fixed-center">
        <q-card style="min-width: 300px">
          <q-img
            src="https://st2.depositphotos.com/3907761/9968/v/950/depositphotos_99683378-stock-illustration-registration-vector-icon.jpg"
            :ratio="4/3"
          />
          <!--
            <q-card-section>
                <div class="q-pa-md flex flex-center text-h6">Registrarse</div>
            </q-card-section>
            -->
            <q-card-section class="q-gutter-xl">
                <q-form @submit="register">
                  <q-input
                        label="Ingrese nombre"
                        v-model="name"
                        :rules="[val => val !== null && val !== '' || 'Por favor llene este campo.']"
                    />
                    <q-input
                        label="Ingrese email"
                        v-model="email"
                        :rules="[val => val !== null && val !== '' || 'Por favor llene este campo.']"
                    />
                    <q-input
                        label="Edad"
                        v-model="age"
                        :rules="[val => val !== null && val !== '' || 'Por favor ingrese nombre de usuario.']"
                    />
                    <q-input
                        label="Contraseña"
                        v-model="password"
                        type="password"
                        :rules="[val => val !== null && val !== '' || 'Por favor ingrese contraseña.']"
                    />
                    <div class="q-pa-md flex flex-center">
                        <q-btn type='sumbit' label='Registrarse'/>
                    </div>
                </q-form>
            </q-card-section>
        </q-card>
    </div>
</template>

<script>
import router from '@/router'
export default {
  name: 'Registro',

  data(){
    return {
      age: '',
      password: '',
      email: '',
      name: ''
    }
  },
  methods: {
    async register() {
      this.$q.loading.show({ delay: 400 })
      let age = this.age
      let password = this.password
      let email = this.email
      let name = this.name
      const post = this.$http.post
      await post(
        '/client/signup',
        {
          name: name, age: age, email: email, password: password
        }
      ).then(res => {
        console.log(res)
        if(res.data){
          this.$q.notify({message: 'Usuario creado!'})
          router.push({name: 'LogIn'})
        } else {
          this.$q.notify({ color: 'negative', message: 'Email ya se encuentra registrado', icon: 'report_problem' })
        }
      }).catch(error => {
        this.$q.notify({ color: 'negative', message: 'Un error ha ocurrido!', icon: 'report_problem' })
      })
      this.$q.loading.hide()
    }
  }
}
</script>
