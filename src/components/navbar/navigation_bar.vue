<template>
    <nav>
        <h3 class="nav-name" >JIDSU</h3>
        <h3 class="contact" >
            <a href="#contact">Hit me up!</a>
        </h3>
    </nav>
</template>
<script setup>
import ScrollReveal from 'scrollreveal';
</script>
<script>


export default {
    mounted(){
        const sr3 = ScrollReveal();
        sr3.reveal('.nav-name', {
        duration:1000,
        origin: 'left',
        distance: '150px',
        easing: 'ease-in-out',
        });
        const sr4 = ScrollReveal();
        sr4.reveal('.contact', {
        duration:1000,
        origin: 'right',
        distance: '150px',
        easing: 'ease-in-out',
        });
    }
}
</script>
<style scoped>
nav{
    position: fixed;
    top:0;
    left:0;

    font-size: 26px;

    z-index: 999;

    display: flex;
    justify-content: space-between;
    align-items: center;

    padding: 5px var(--border-padding) 5px var(--border-padding) ;
    box-sizing: border-box;


    width: 100%;
    height: var( --main-nav-bar-height);
    color:var(--light-brown);
    background-color: transparent;
}
nav h3 a{
    text-decoration: none;
    color: var(--light-brown);
    cursor: pointer;
}

@media (max-width: 600px) {
    nav{
        font-size: 18px;
        padding: 5px var(--border-phone) 5px var(--border-phone) ;
    }
}

</style>