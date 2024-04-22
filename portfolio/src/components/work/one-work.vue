<template>
    <div class="one-work" >
        <div class="description">
            <div class="top">
                <h4>
                    <slot name="projectName" ></slot>
                </h4>
                <p>
                    <slot name="projectDescription" ></slot>
                </p>
            </div>
            <div class="bottom">
                <p class="line" >
                    <span>Role</span>
                    <span class="line-value" >
                        <slot name="Role" ></slot>
                    </span>
                </p>
                <p class="line">
                    <span>Visit Website</span>
                    <slot name="projectUrl" ></slot>
                </p>
                <p class="line"> 
                    <span>Technologies</span>
                    <span class="line-value" >
                        <span v-for="Technologie,index in Technologies" :key="index">
                             {{ index == Technologies.length-1 ? Technologie  : Technologie + ', ' }}
                        </span>
                    </span>
                </p>
            </div>
        </div>
        <div class="mockups scrollbar-element">
            <slot name="mockups" ></slot>
        </div>
    </div>
</template>
<script setup>
import ScrollReveal from 'scrollreveal';
</script>
<script>
export default{
    props : {
        projectUrl : String,
        Technologies : Array
    },
    mounted(){
        const sr3 = ScrollReveal();
        sr3.reveal('.description', {
        duration:600,
        origin: 'left',
        distance: '500px',
        easing: 'ease-in-out',
        });
        const sr4 = ScrollReveal();
        sr4.reveal('.mockups', {
        duration:600,
        origin: 'right',
        distance: '500px',
        easing: 'ease-in-out',
        });
    }
}
</script>
<style >

.one-work{
    display: flex;
    justify-content: center;
    align-items: flex-start;


    min-height: var(--section-height);
    width: 100%;
}
.one-work .description{
    flex-grow: 1;
    width: 60%;

    min-height: 600px;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;

    padding: 10px;
    box-sizing: border-box;

}
.one-work .description .top{
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;

    gap: 24px;

    text-align: left;
}
.one-work .description .top h4{
    font-size: 30px;
}
.one-work .description .top p{
    font-size: 20px;
}
.one-work .mockups{
    width: 100%;

    min-height: 600px;
    max-height: 600px;
    overflow-y: auto;

    border-radius: 7px;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;

    gap: 24px;
    padding: 24px;
    box-sizing: border-box;
   
    background-color: #333333;
    opacity: 0.7;
    background-image:  repeating-radial-gradient( circle at 0 0, transparent 0, #333333 40px ), repeating-linear-gradient( #E8E1D955, #E8E1D9 );
}
.one-work .mockups .mockup{

    width: 100%;
    min-height: 550px;

    background-color: red;

    background-size: cover; 
    background-position: center center; 
    background-repeat: no-repeat; 

    border-radius: 14px;
}
.one-work .description .bottom{
    width: 100%;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    gap: 10px;
    padding-top: 10px;
    box-sizing: border-box;

    border-top: solid 1px var( --light-brown);

}
.one-work .description .bottom p{
    font-size: 16px;
    line-height: 40px;
}
.one-work .description .bottom .line-value{
    width: 50%;
    text-align: left;
    text-decoration: none;
    color: var(--light-brown);
}
.one-work .description .bottom .line{
    display: flex;
    justify-content: space-between;
    align-items: center;

    border-bottom: solid 1px var( --light-brown);

    width: 100%;
}
@media (max-width: 1200px) {
    .one-work{
        flex-direction: column;
        gap: 50px;
    }
    .one-work .description{
        min-height: auto;
        gap: 50px;
        width: 100%;
    }
    .one-work .description .top p{
        font-size: 18px;
    }
    .one-work .description .bottom p{
    font-size: 14px;
    line-height: 40px;
}
}
</style>