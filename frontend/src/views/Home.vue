<template>
    <b-container fluid class="v-home">
        <b-card>
            <h3>Thank you for participating in the AirStorage prototype survey</h3>
                On the next page, you will be presented with four possible listings.<br>
                Out of these four options, please select the listing you <i>trust most</i>.<br>
                After, you will be asked to fill in a short (~5 minutes) survey of your experience.<br>
                Please press the button to start:<br><br>
                <b-button variant="success" to="listings">Start</b-button>
        </b-card>
    </b-container>
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
</style>
