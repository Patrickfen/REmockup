<template>
    <b-card no-body class="overflow-hidden">
        <b-row no-gutters class="properties">
            <picture-chooser :images="prop_listing.Image"></picture-chooser>
            <b-col md="6" @click="choose()">
                <badge class="badge" v-if="prop_listing.Verified == 'True'" />
                <b-card-body :title="prop_listing.Name">
                    <prop-text :prop_listing="prop_listing">
                    </prop-text>
                    <star :value="prop_listing.Stars" class="star"/>
                    <review-list :reviews="prop_listing.Review"/>
                </b-card-body>
            </b-col>
        </b-row>
    </b-card>
</template>

<script>
import text from "./Listing-text.vue"
import star from "./Score.vue"
import pictureChooser from "./VPictureChooser.vue"
import reviewList from "./VReviewList.vue"
import badge from "./VBadge.vue"
    export default {
        name: 'listings',
        data() {
            return {
            }
        },
        props: {
            prop_listing: {
                type: Object,
                required: true
            }
        },
        components: {
            "prop-text": text,
            "star": star,
            "picture-chooser": pictureChooser,
            "review-list" : reviewList,
            "badge" : badge
        },
        mounted(){
        },
        methods: {
            choose() {
                this.$parent.choose(this.prop_listing)
            }
        }
    }
</script>

<style scoped lang="scss">
    .properties:hover {
        background-color: lightgray;    
        cursor: pointer;
    }
    .badge {
        float: right;
        margin-right: 30px;
        margin-top: 10px
    }

    .star {
        margin-left: 25px;
    }
</style>
