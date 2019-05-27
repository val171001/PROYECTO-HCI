<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated class="glossy">
      <q-toolbar color="amber" text-color="dark" inverted>
        <q-toolbar-title color='red'>
          Maquina para Salvar el Mundo
        </q-toolbar-title>

        <div></div>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view/>
    </q-page-container>
  </q-layout>
</template>

<script>


export default {
  name: 'LayoutDefault',
}
</script>

<style>
</style>
