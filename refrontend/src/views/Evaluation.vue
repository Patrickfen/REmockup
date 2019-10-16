<template>
    <b-container>
       <iframe class="eval" src="https://docs.google.com/forms/d/e/1FAIpQLSfeT7bncpxv4Dn3rhB99Qak1gm_xOxvzmzsdV30XTQpzQ5W4w/viewform?embedded=true">
            Loading…
        </iframe>
    </b-container>    
</template>

<script>
    export default {
        name: 'evaluation',
        mounted(){
        }
    }
</script>

<style scoped lang="scss">
// Occupy entire screen.
.eval {
    position: fixed; 
    top: 0; 
    left: 0; 
    bottom: 0; 
    right: 0; 
    width: 100%; 
    height: 100%; 
    border: none; 
    margin: 0; 
    padding: 0; 
    overflow: hidden; 
    z-index:999999;
}
</style>
