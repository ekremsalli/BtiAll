<template>
  <div id="q-app">
    <router-view />
  </div>
</template>
<script>
export default {
  name: 'App'
}
window.addEventListener('load', function(event){
  console.log('%cBTI http://www.btidanismanlik.com', 'color: red; font-size: 10px; font-weight: bold;');
})
</script>
