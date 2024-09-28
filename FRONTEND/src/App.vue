<template>
  <div>
    <NavBar /> 
    <router-view />
    <BottomBar />
  </div>
</template>

<script>
// import Vue  from 'vue'
import NavBar from '@/components/NavBar.vue'
import BottomBar from '@/components/BottomBar.vue'


export default {
  name: 'App',
  components: {
    NavBar, BottomBar
  }
}

</script>

<style>
body {
  background: #526d82;
  font-family: "Roboto Mono", monospace;
}
.custom-container {
  background: #9db2bf;
  max-width: 30%;
  min-height: 325px;
  margin-top: 50px;
  border-radius: 10px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}
</style>
