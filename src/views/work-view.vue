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
                Lorem ipsum, dolor sit amet consectetur adipisicing elit. Rerum quo, quidem numquam consectetur sequi modi aut magni reprehenderit,
                eaque facilis odio adipisci est, repudiandae laudantium? Quas suscipit officia veritatis? Reiciendis?
            </template>
            <template #Role >
                Front-end developer
            </template>
            <template #projectUrl >
                <a href="https://mafaldental.netlify.app/" target="_blank" class="line-value" >mafaldental.netlify.app</a>
            </template>
            <template #mockups>
                <div :style="{backgroundImage : `url(${mafal})`}" class="mockup"></div>
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