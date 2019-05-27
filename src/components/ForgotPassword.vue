<template>
    <div>
        <q-btn
            label='¿Olvido su contraseña?'
            size='sm'
            color='positive'
            @click="show = !show"
        />
        <q-dialog v-model="show">
            <q-card style="min-width: 300px">
                <q-card-section>
                    <div class="q-pa-md flex flex-center text-h6">Recuperar contraseña</div>
                </q-card-section>
                <q-card-section>
                    <q-input
                        label="Ingrese su correo electronico"
                        v-model="email"
                        :rules="[val => val !== null && val !== '' || 'Por favor ingrese nombre de usuario.']"
                    />
                </q-card-section>
                <q-card-section>
                    <div class="q-pa-md flex flex-center">
                        <q-btn label="Aceptar" @click="handle"/>
                    </div>
                    <div class="q-pa-md flex-center">
                      <q-btn align="around" class="btn-fixed-width" color="negative" label="Cancelar" icon="img:https://cdn.pixabay.com/photo/2012/04/12/19/41/red-30336_960_720.png" @click="show = !show"/>
                    </div>
                </q-card-section>
                <q-card-section>
                    <div class="q-pa-md flex flex-center">
                        <span>{{password}}</span>
                    </div>
                </q-card-section>
            </q-card>
        </q-dialog>
    </div>
</template>
<script>
  import router from '@/router'
export default {
    name: 'ForgotPassword',
    data(){
        return {
            show: false,
            email: '',
            password: ''
        }
    },
    methods: {
        async handle(){
            this.$q.loading.show({ delay: 400 })
            const post = this.$http.post
            let email = this.email
            await post(
                '/client/verify/email',
                {
                email: email
                }
            ).then(results => {
                this.password = 'Su contraseña es: ' + results.data[0].password
            }).catch(error => {
                this.$q.notify({ color: 'negative', message: 'Email no encontrado', icon: 'report_problem' })
            })
            this.$q.loading.hide()
        },
        login() {
          router.push({name: 'LogIn'})
        }
    }
}
</script>
