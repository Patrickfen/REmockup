<template>
    <div class="v-verified-badge">
        <i
            v-b-tooltip.hover title="This person has passed the background check and is verified" 
            class="fa fa-check-circle-o fa-3x">
        </i>
    </div>
</template>

<script>
    export default {
        name: 'v-verified-badge'
    }
</script>

<style scoped lang="scss">
    .v-verified-badge{
        .fa{color:#238ae6;}
    }
</style>
