<template>
    <b-col md="6" class="v-picture-chooser" :style="{backgroundImage: 'url(' + images[chosen] + ')'}" 
        v-on:click.self="$parent.choose()">
        <div class="thumbnails" v-if="images.length > 1">
            <template v-for="(img, idx) in images">
                <img :src="img" @click="chosen=idx"></img>
            </template>
        </div>
    </b-col>
</template>

<script>
    export default {
        name: 'v-picture-chooser',
        data(){
            return{
                chosen:0,
                halfSize:1
            }
        },
        props: [
            'images',
        ],
        mounted(){
        },
    }
</script>

<style scoped lang="scss">
.v-picture-chooser {
    position:relative;
    padding:0;
    margin:0;
    padding-bottom:50%;


    display: inline-block;
    width:100%;
    background-position: center center;
    background-size: cover;
    background-repeat: no-repeat;
    border-radius:5px;

    .thumbnails {
        position:absolute;
        bottom:0;
        width:100%;
        overflow-x: hidden;

        img {
            cursor:pointer;
            width:70px;
            height:70px;
            margin:5px;
            border:2px solid #fff;
            border-radius:3px;
        }
    }
}
</style>
