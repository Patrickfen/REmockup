<template>
    <b-container>
        <span v-for="n in 5" :key="n">
            <span class="fa fa-star" v-bind:class="{ checked: value >= n}"></span>
        </span>
    </b-container>
</template>

<script>
    export default {
        name: 'score',
        props: { 
            value: {
                type: Object,
                required: true
            }
        }
    }
</script>

<style scoped lang="scss">
.checked {
  color: orange;
}
</style>