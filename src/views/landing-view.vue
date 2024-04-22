<template>
    <div class="landing-div big-titel">
        <p class="my-name" >
            JIDSU
        </p>
        <h1 class="job-desc" >
            <span style="white-space:wrap;">web developer</span>
        </h1>
        <h4 class="motivation" style="white-space:wrap;">here to craft simple and useful experiences.</h4>
        <div class="bottom-line">
            <p>FULL STACK WEB DEVELOPER</p>
            <div class="social-media">
                <github class="small-icons" />
                <instagram class="small-icons" />
                <linkedin class="small-icons" />
            </div>
        </div>
    </div>

</template>
<script setup>
import ScrollReveal from 'scrollreveal';
</script>
<script>


import github from "../components/svgs/github-icon.vue"
import instagram from "../components/svgs/instagram-icon.vue"
import linkedin from "../components/svgs/linkedin-icon.vue"
export default {
    components: {
        github,
        instagram,
        linkedin
    },
    mounted(){
        const sr3 = ScrollReveal();
        sr3.reveal('.my-name', {
        duration:600,
        origin: 'bottom',
        distance: '150px',
        easing: 'ease-in-out',
        });
        const sr1 = ScrollReveal();
        sr1.reveal('.job-desc', {
        duration:800,
        origin: 'bottom',
        distance: '150px',
        easing: 'ease-in-out',
        });
        const sr2 = ScrollReveal();
        sr2.reveal('.motivation', {
        duration:1000,
        origin: 'bottom',
        distance: '150px',
        easing: 'ease-in-out',
        });
        const sr5 = ScrollReveal();
        sr5.reveal('.bottom-line', {
        duration:1000,
        origin: 'bottom',
        distance: '150px',
        easing: 'ease-in-out',
        });
    }
}
</script>

<style scoped>
.landing-div .my-name{

}
.landing-div {

    height: calc(100vh - var(--main-nav-bar-height));
    width: 100%;
    min-height: 400px;


    position: relative;
    left: 0;
    margin-top: var(--main-nav-bar-height);

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;

    padding: 0px 50px 0% 50px;
    box-sizing: border-box;

    text-align: center;
    color: var(--light-brown);
    
}

.bottom-line {
    position: absolute;
    font-size: 20px;

    bottom: 0;
    left: 0;
    width: 100%;

    z-index: 999;

    display: flex;
    justify-content: space-between;
    align-items: center;

    padding: 15px var(--border-padding) 15px var(--border-padding);
    box-sizing: border-box;

    color: var(--light-brown);

    white-space: nowrap;
}

.bottom-line .social-media {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 15px;
    box-sizing: border-box;
}

.bottom-line .social-media svg:hover {
    font-size: 40px;
    cursor: pointer;
}

@media (max-width: 600px) {
    .landing-div {
        font-size: 30px;

    }

    .bottom-line {
        font-size: 14px;
        padding: 15px var(--border-phone) 15px var(--border-phone);
    }
}
@media (max-width: 400px) {
    .landing-div {
        font-size: 24px;

    }

    .bottom-line {
        font-size: 12px;
        padding: 15px var(--border-phone) 15px var(--border-phone);
    }
}
@media (max-width: 350px) {
    .landing-div {
        font-size: 20px;

    }

    .bottom-line {
        font-size: 10px;
        padding: 15px var(--border-phone) 15px var(--border-phone);
    }
}
@media (max-width: 300px) {
    .landing-div {
        font-size: 20px;
    }
}
</style>
