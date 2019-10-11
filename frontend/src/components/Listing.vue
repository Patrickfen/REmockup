<template>
    <b-card no-body class="overflow-hidden">
        <b-row no-gutters>
            <picture-chooser :images="prop_listing.Image"></picture-chooser>
            <b-col md="6">
                <b-card-body :title="prop_listing.Name">
                    <prop-text :prop_listing="prop_listing">
                    </prop-text>
                    <star :value="prop_listing.Stars">
                    </star>
                </b-card-body>
            </b-col>
        </b-row>
    </b-card>
</template>

<script>
import text from "./Listing-text.vue"
import star from "./Score.vue"
import pictureChooser from "./VPictureChooser.vue"
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
            "picture-chooser": pictureChooser
        },
        mounted(){
            /*var ctx = this;
            window.addEventListener('resize', function(){
                ctx.halfSize = ctx.$refs.listingContainer.clientHeight / 2;
            });
            ctx.halfSize = ctx.$refs.listingContainer.clientHeight / 2;*/
        }
    }
</script>

<style scoped lang="scss">
</style>
