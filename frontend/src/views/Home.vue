<template>
    <div class="banner">
        <div class="rounded banner-text col-md-5 col-sm-10">
            <div class="logo">

            </div>
            <h3>Thank you for participating in the AirStorage prototype survey</h3>
            <p>
                On the next page, you will be presented with four possible listings.<br>
                Out of these four options, please select the listing you <i>trust most</i>.<br>
                After, you will be asked to fill in a short (~5 minutes) survey of your experience.<br>
                Please press the button to start:<br><br>
            </p>
                <b-button pill class="start" variant="success" to="listings">Start</b-button>
        </div>
    </div>
    <!-- <b-container fluid class="v-home">
    </b-container> -->
</template>

<script>
    export default {
        name: 'home',
    }
</script>

<style scoped lang="scss">
.v-home{
    padding-top:80px;
}

.banner {
    background-image: url('../assets/banner.jpg');
    background-position: center;
    background-size: cover;
    height: 100vh
}

.banner-text {
    color: white;
    background-color: rgba(0,0,0,0.55);
    margin: auto;
    width: 50%;
    padding: 20px;
    margin-top: 3rem;
    text-align: center;
    font-size: 18px;
}

.start {
    margin: 0 auto;
    width: 50%;
    text-align: center;
}

.logo {
    background-image: url("../assets/airstorage.png");
    background-position: center;
    background-size: cover;
    
}

@media (min-width: 0px) {
    .logo {
        height: 7vh !important;
    }
}

@media (min-width: 782px) {
    .logo {
        height: 210px;
    }
}
</style>
