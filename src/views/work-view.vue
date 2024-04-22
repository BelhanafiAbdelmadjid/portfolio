<template>
    <section class="work-section">
        <h1 class="big-titel my-project-titel">
            <span style="white-space:wrap;" >My projects</span>
        </h1>
        <workSection
        :projectUrl="String()"
        :Technologies="['Vue','JS']" >
            <template #projectName >
                Mafal dental    
            </template>
            <template #projectDescription >
                Mafal Dental is a newly established dental clinic, founded in 2023. As a web developer, 
                it was my responsibility to contribute to its growth by creating a showcase page. This page allows clients to access comprehensive information about
                the clinic and showcases the services they provide through an intuitive UI/UX design.
            </template>
            <template #Role >
                Front-end developer
            </template>
            <template #projectUrl >
                <a href="https://mafaldental.netlify.app/" target="_blank" class="line-value" >mafaldental.netlify.app</a>
            </template>
            <template #mockups>
                <img class="mockup-image" :src="mafal" alt="mockup-mafal-dental-clinique">
            </template>
            
        </workSection>
    </section>
</template>
<script setup>
import ScrollReveal from 'scrollreveal';
</script>
<script>
import workSection from "../components/work/one-work.vue"
import mafal from '../assets/images/projects/mafal-dental/mafal-dental-mockup.png'
export default{
    data(){
        return{
            mafal : mafal
        }
    },
    components : {
        workSection
    },
    mounted(){
        const sr3 = ScrollReveal();
        sr3.reveal('.my-project-titel', {
        duration:600,
        origin: 'bottom',
        distance: '150px',
        easing: 'ease-in-out',
        });
        
        const sr4 = ScrollReveal();
        sr4.reveal('.mockup-image', {
        duration:1000,
        origin: 'right',
        distance: '500px',
        easing: 'ease-in-out',
        });
       
    }
}
</script>
<style scoped >
.work-section{
    min-height: calc(100vh - var(--main-nav-bar-height));
    width: 100%;
    min-height: 400px;


    position: relative;

    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    flex-wrap: wrap;

    gap: 70px;

    padding: 5px var(--border-padding) 5px var(--border-padding) ;
    box-sizing: border-box;

    text-align: center;
    color: var(--light-brown);
    font-size: 40px;
}
@media (max-width: 600px) {
    .work-section {
        padding: 15px var(--border-phone) 15px var(--border-phone);
    }
}
</style>