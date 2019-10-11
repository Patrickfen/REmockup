<template>
    <b-row class="no-r-margin">
        <listing class="col-md-6" v-for="prop_listing in prop_listings" :prop_listing="prop_listing" :key="prop_listing">
        </listing>
    </b-row>
</template>

<script>
import listing from "./Listing.vue"
    export default {
        name: 'listings',
        data() {
            return {
                prop_listings : [
                {
                    "Name" : "Storage Minnesota",
                    "Owner" : "Patricia",
                    "Cost" : "20 $ / Month",
                    "Availability" : "Weekly",
                    "Security": "GPS / Camera Available",
                    "Image": "https://picsum.photos/400/400/?image=20",
                    "Stars" : 5
                }, 
                {
                    "Name" : "Storage Minnesota",
                    "Owner" : "Patricia",
                    "Cost" : "20 $ / Month",
                    "Availability" : "Weekly",
                    "Security": "GPS / Camera Available",
                    "Image": "https://picsum.photos/400/400/?image=20",
                    "Stars" : 4
                },
                {
                    "Name" : "Storage Minnesota",
                    "Owner" : "Patricia",
                    "Cost" : "20 $ / Month",
                    "Availability" : "Weekly",
                    "Security": "GPS / Camera Available",
                    "Image": "https://picsum.photos/400/400/?image=20",
                    "Stars" : 4
                }, 
                {
                    "Name" : "Storage Minnesota",
                    "Owner" : "Brick",
                    "Cost" : "20 $ / Month",
                    "Availability" : "Weekly",
                    "Security": "GPS / Camera Available",
                    "Image": "https://picsum.photos/400/400/?image=20",
                    "Stars" : 2
                }
                ]
            }
        },
        props: {
            // prop_listings: {
            //     type: Object,
            //     required: true
            // }
        },
        components: {
            'listing': listing
        }
    }
</script>

<style scoped lang="scss">
    listing {
        height: 50%;
    }

    .no-r-margin {
        margin-right: 0;
    }
</style>
