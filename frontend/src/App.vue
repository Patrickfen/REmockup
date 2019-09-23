<template>
    <div>
        <router-view/>
    </div>
</template>

<script>
export default {
    name: 'app',
    created(){
        console.log('App init');
    }
}
</script>

<style lang="scss">

</style>
