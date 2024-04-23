
<template>
    <section class="about">
        <h1 id="about" class="big-titel" >About me</h1>
        <div class="content-about">
            <div class="my-picture"></div>
            
            <p>
                <span>
                    Lorem ipsum, dolor sit amet consectetur adipisicing elit. Itaque accusamus expedita aspernatur pariatur quaerat modi? Consectetur quo voluptatum soluta placeat quae laudantium aliquid tempore nisi. Molestias ducimus voluptate ad labore officia, fugiat corporis nobis blanditiis hic? 
                </span>
                <span>
                    Ab reprehenderit vel laudantium, enim maxime minus culpa doloribus reiciendis consectetur est, inventore aspernatur.
                </span>
            </p>
        </div>
    </section>
</template>
<script>
export default{

}
</script>
<style scoped>
.about{
    position: relative;
    min-height: 400px;
    height: calc(100vh - var(--main-nav-bar-height));
    width: 100%;

    margin-top: var(--main-nav-bar-height);

    display: block;
    place-content: center;
    /* row-gap: 25px; */

    padding: 40px;
    box-sizing: border-box;

}
.about .my-picture{

    filter: grayscale(0.6);
    border-radius: 50%;

    position: relative;
    background-image: url('../assets/images/me/my_picture.jpeg');

    background-size: cover; 
    background-position: center center; 
    background-repeat: no-repeat; 

    min-height: 300px;
    min-width: 300px;

}
.about p{
    font-size: 20px;
    font-weight: 500;
    color: var( --light-brown);
    text-align: left;
}
.about h1{
    margin-bottom: 50px;
}
.about .content-about{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: flex-start;

    gap: 15px;

    width: 100%;
    min-height: 400px;
}
.about .content-about p{
    width: 50%;

    height: 100%;
    min-height: 300px;

    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: center;

}

@media (max-width: 800px) {
    .about{
        margin-bottom: 50px;
        min-height: 600px;

        padding-left: 16px ;
        padding-right: 16px ;
    }
    .about .content-about{
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;

        gap: 24px;

        width: 100%;
    }
    .about .content-about p{
        width: 100%;

        text-align: center;
        font-size:16px;

    }
    .about h1{
        margin-top: 50px;
    }

}
@media (max-width: 400px) {

    .about .my-picture{
        min-width: 200px;
        min-height: 200px;
    }


}
</style>