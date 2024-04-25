<template>
    <div class="skill-card">
        <slot name="image" ></slot>
        <p>{{ skillName }}</p>
    </div>
</template>

<script>
export default{
    props : ['skillName', 'image']
}
</script>

<style scoped>

.skill-card{
    /* flex-grow: 0;  */
    /* flex-shrink: 1;  */
    /* flex-basis: 200px; */

    width: 200px;
    min-width: 200px;
    min-height: 200px;
    height: 200px;

    border-radius: 10px;

    background-color: var(--light-brown);

    transition: all 0.25s;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    gap: 16px;
}
.skill-card:hover{
    scale: 1.1;
}
@media (max-width: 800px) {
    .skill-card{
        width: 150px;
        min-width: 150px;
        min-height: 150px;
        height: 150px;
    }
}
@media (max-width: 600px) {
    .skill-card{
        width: 125px;
        min-width: 125px;
        min-height: 125px;
        height: 125px;
    }
}

</style>

