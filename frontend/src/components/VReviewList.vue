<template>
    <b-list-group class="v-review-list">
        <b-list-group-item v-for="(rev, idx) in reviews" :key="idx">
            <b>{{rev.author}}</b><i class="time">{{rev.time}}</i><br>
            <i class="fa fa-quote-left"></i>
            <i class="comment">{{rev.text}}</i>
            <i class="fa fa-quote-right"></i>
        </b-list-group-item>
    </b-list-group>
</template>

<script>
    export default {
        name: 'v-review-list',
        props:[
            'reviews'
        ]
    }
</script>

<style scoped lang="scss">
    .v-review-list{
        position:relative;
        width:100%;
        .time{
            float:right;
            color:#8b8b8b;
        }
        .fa{
            color:#8b8b8b;
        }
        .comment{
            margin:0 15px;
        }
    }
</style>
