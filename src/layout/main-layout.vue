<template>
    <navbar />
    <background></background>
    <div class="layout-content" style="width: 100%;"   >
      <slot name="content">
      </slot>
    </div>
    <footerComp/>
</template>
<script>
import navbar from "../components/navbar/navigation_bar.vue"
import background from "../components/back-ground.vue"
import footerComp from "../components/footer/footer-view.vue"
export default {
  name: 'main-layout',
  components: {
    navbar,
    background,
    footerComp
  }
}
</script>
<style scoped>
.layout-content{
  background-color: var(--dark-gray);


  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 15vh;
}

.scrollbar-element::-webkit-scrollbar {
    width: 5px; 
}

/* Track */
.scrollbar-element::-webkit-scrollbar-track {
    background: red; 
}

/* Handle */
.scrollbar-element::-webkit-scrollbar-thumb {
    background: #ba1a1a; 
    border-radius: 10px; 
}

</style>