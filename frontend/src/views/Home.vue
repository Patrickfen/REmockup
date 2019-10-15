<template>
    <div class="banner">
        <div class="rounded banner-text col-md-6 col-sm-8">
            <b-img class="logo" fluid :src="require('../assets/airstorage.png')" />
            <h3>Thank you for participating in the AirStorage prototype survey</h3>
            <p>
                On the next page, you will be presented with 4 or less listings.<br>
                Out of these options, please select the listing you think is the most <i>trustworthy</i>.<br>
                After, you will be asked to fill in a short (~5 minutes) survey of your experience.<br>
                Please press the button to start:<br><br>
            </p>
                <b-button pill class="start" variant="primary" to="listings">Start</b-button>
        </div>
    </div>
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
    // width: 50%;
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
    
}

// @media (min-width: 0px) {
//     .logo {
//         height: 7vh;
//     }
// }

// @media (min-width: 782px) {
//     .logo {
//         height: 210px;
//     }
// }
</style>
