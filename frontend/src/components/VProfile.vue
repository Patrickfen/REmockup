<template>
    <div class="profile rounded" :style="{backgroundImage: 'url(' + this.url + ')'}">
    </div>
</template>

<script>
    export default {
        name: 'v-profile-picture',
        props: [
            'url',
        ],
    }
</script>

<style scoped lang="scss">
.profile {
    min-height: 140px;
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
    margin: 0 10px 0 20px;
}
</style>
