<template>
    <b-card no-body class="overflow-hidden">
        <b-row no-gutters>
            <b-col md="6">
                <b-card-img :src="prop_listing.Image" class="rounded-0"></b-card-img>
            </b-col>
            <b-col md="6" class = "properties" @click="choose(prop_listing)">
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
    export default {
        name: 'listings',
        data() {
            return {
                "" : ""
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
            "star": star
        },
        methods: {
            choose(listing) {
                console.log(listing.Cost)
            }
        }
    }
</script>

<style scoped lang="scss">
.properties:hover {
    background-color: lightgray;    
    cursor: pointer;
}
</style>
