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
                <q-form @submit="">
                    <q-input
                        label="Ingrese email"
                        v-model="email"
                        :rules="[val => val !== null && val !== '' || 'Por favor llene este campo.']"
                    />
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
                    <q-input
                        label="Ingrese nuevamente su contraseña"
                        v-model="password"
                        type="password"
                        :rules="[val => val !== null && val !== '' || 'Por favor ingrese contraseña.']"
                    />
                    <div class="q-pa-md flex flex-center">
                        <q-btn type="submit" label="Iniciar sesion"/>
                        <q-btn type='sumbit' label='Registrarse'/>
                    </div>
                </q-form>
            </q-card-section>
        </q-card>
    </div>
</template>

<style>
</style>

<script>
export default {
  name: 'Registro',

  data(){
    return {
      username: '',
      password: '',
      email: ''
    }
  }
}
</script>
