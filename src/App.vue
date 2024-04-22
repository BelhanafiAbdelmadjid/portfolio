<template>  
  <mainLayout>
    <template #content >
        <landing/>
        <work/>
      </template>
    </mainLayout>
</template>

<script>
import mainLayout from "./layout/main-layout.vue"

import landing from "./views/landing-view.vue"
import work from "./views/work-view.vue"
export default {
  name: 'App',
  components: {
    mainLayout,
    landing,
    work,
  }
}
</script>
<style src='./assets/css/main.css'></style>
<style>

</style>
