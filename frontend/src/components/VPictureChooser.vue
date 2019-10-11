<template>
    <b-container class="v-picture-chooser" :style="{'width': size + 'px', 'height': size + 'px'}">
        <img class="chosen" :src="images[chosen]"></img>
        <div class="thumbnails" v-if="images.length > 1">
            <template v-for="(img, idx) in images">
                <img :src="img" @click="chosen=idx"></b-img>
            </template>
        </div>
    </b-container>
</template>

<script>
    export default {
        name: 'v-picture-chooser',
        data(){
            return{
                chosen:0
            }
        },
        props:[
            'images',
            'size'
        ]
    }
</script>

<style scoped lang="scss">
.v-picture-chooser{
    position:relative;
    padding:0;
    margin:0;

    img.chosen{
        width:100%;
        height:100%;
        object-fit: cover;
        border-radius:5px;
    }
    .thumbnails{
        position:absolute;
        bottom:0;
        width:100%;
        overflow-x: hidden;
        img{
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
