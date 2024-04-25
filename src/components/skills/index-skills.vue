<template>

    <section class="skills">
        <h1 class="big-titel" >What I'm good at</h1>
        <div class="cards">
            <card :skillName="'Python'"   >
                <template #image >
                    <img class="card-image" :src="python" alt="Python logo">
                </template>
            </card>
            <card :skillName="'Django'" >
                <template #image >
                    <img class="card-image" :src="django" alt="Django logo">
                </template>
            </card>
            <card :skillName="'Flask'" >
                <template #image >
                    <img class="card-image" :src="flask" alt="Flask logo">
                </template>
            </card>
            <card :skillName="'Vue'" >
                <template #image >
                    <img class="card-image" :src="vue" alt="Vue logo">
                </template>
            </card>
            <card :skillName="'Nuxt'" >
                <template #image >
                    <img class="card-image" :src="nuxt" alt="Nuxt logo">
                </template>
                
            </card>
            <card :skillName="'Tailwind'" >
                <template #image >
                    <img class="card-image" :src="tailwind" alt="Tailwind logo">
                </template>
            </card>
            <card :skillName="'Laravel'" >
                <template #image >
                    <img class="card-image" :src="laravel" alt="Laravel logo">
                </template> 
              
            </card>
            <card :skillName="'MySql'" >
                <template #image >
                    <img class="card-image" :src="mysql" alt="MySql logo">
                </template> 
            </card>
            <card :skillName="'Docker'" >
                <template #image >
                    <img class="card-image" :src="docker" alt="Docker logo">
                </template>
            
            </card>
            <card :skillName="'Blender'" >
                <template #image >
                    <img class="card-image" :src="blender" alt="Blender logo">
                </template>
                
            </card>
            <card :skillName="'Three'" >
                <template #image >
                    <img class="card-image" :src="three" alt="Three logo">
                </template>
            </card>
        </div>
    </section>

</template>
<script>
import card from "./skills-card.vue"

import python from "../../assets/images/skills/python.png"
import docker from "../../assets/images/skills/docker.png"
import laravel from "../../assets/images/skills/Laravel.png"
import mysql from "../../assets/images/skills/mysql.png"
import vue from "../../assets/images/skills/vue.png"
import blender from "../../assets/images/skills/blender.png"
import three from "../../assets/images/skills/three.png"
import django from "../../assets/images/skills/django.png"
import nuxt from "../../assets/images/skills/nuxt.png"
import tailwind from "../../assets/images/skills/tailwind.png"
import flask from "../../assets/images/skills/flask.jpg"
export default{
    data(){
        return {
            python : python,
            docker : docker,
            laravel : laravel,
            mysql : mysql,
            vue : vue,
            blender : blender,
            three:three,
            django:django,
            nuxt:nuxt,
            tailwind:tailwind,
            flask:flask
        }
    },
    components : {
        card
    }
}
</script>
<style >
.skills{
    position: relative;


    padding-left: var(--border-padding);
    padding-right: var(--border-padding);
    box-sizing: border-box;
}
.skills h1{
    margin-bottom: 50px;
}
.skills .cards{

    height: auto;

    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;

    gap: 50px;

}
.card-image{
    height: 30%;
    width: auto;

    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;

}
.card-image img{
    width: 100%;
    height: auto;
}
</style>    