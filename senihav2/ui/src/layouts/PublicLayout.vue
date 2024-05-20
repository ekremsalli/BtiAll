<template>
  <q-layout view="lHh Lpr lFf">
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
export default {
  mounted(){
    this.$q.loading.hide()
  }
}
</script>

<style lang="css" scoped>
</style>
