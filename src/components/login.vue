<template>
  <div class="fixed-center">
        <q-card style="min-width: 300px">
            <q-card-section>
                <div class="q-pa-md flex flex-center text-h6">Iniciar Sesion</div>
            </q-card-section>
            <q-card-section class="q-gutter-xl">
                <q-form @submit="">
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
                        <q-btn type="submit" label="Iniciar sesion"/>
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
  name: 'Login',

  data(){
    return {
      username: '',
      password: ''
    }
  }
}
</script>
