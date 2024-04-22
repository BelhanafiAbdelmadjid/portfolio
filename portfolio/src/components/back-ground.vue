<template>
    <div class="magicpattern background scrollbar-element" >

    </div>
</template>
<style scoped>
.background {
    height: 100%;
    width: 100%;



    position: absolute;
    left: 0;
    bottom: 0;

    animation: fade-in 0.5s ease-in ;


}
@keyframes fade-in {
    0%{
        opacity: 0;
    }
    100%{
        opacity: 1;
    }
}
</style>