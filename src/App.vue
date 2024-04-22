<template>  
  <mainLayout>
    <template #content >
        <Router-view></Router-view>
      </template>
    </mainLayout>
</template>

<script>
import mainLayout from "./layout/main-layout.vue"

export default {
  name: 'App',
  components: {
    mainLayout,
  }
}
</script>
<style src='./assets/css/main.css'></style>
<style>

</style>
