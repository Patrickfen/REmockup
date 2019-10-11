<template>
    <router-view class="overflow-hidden" />
</template>

<script>
export default {
    name: 'app',
    created() {
        console.log('App init');
    }
}
</script>

<style lang="scss">
@import 'node_modules/bootstrap/scss/bootstrap';
@import 'node_modules/bootstrap-vue/src/index.scss';
</style>
