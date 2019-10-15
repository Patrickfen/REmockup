

<template>
    <ul>
        <li v-if="prop_listing.Owner != ''"><b>Name:</b> {{prop_listing.Owner}}</li>
        <li v-if="prop_listing.Availability != ''"><b>Availability:</b> {{prop_listing.Availability}}</li>
        <li v-if="prop_listing.Security != ''"><b>Security:</b> {{prop_listing.Security}}</li>
    </ul>
</template>

<script>
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
        }
    }
</script>

<style scoped lang="scss">
    ul {
        list-style-type: "";
        padding-left: 0px;
    }
</style>
