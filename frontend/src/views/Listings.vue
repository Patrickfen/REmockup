<template>
    <b-row class="no-r-margin">
        <listing class="col-md-6" v-for="prop_listing in prop_listings" :prop_listing="prop_listing" :key="prop_listing">
        </listing>
    </b-row>
</template>

<script>
import listing from "../components/Listing.vue"
import dataset from "@/assets/dataset.json"
    export default {
        name: 'listings',
        data() {
            return {
                last : false,
                prop_listings : [],
                order : {},
                pool : dataset
            }
        },
        mounted() {
            this.prop_listings = this.shuffle(this.pool).slice(0,4);
            for (let i = 0; i < this.pool.length; i++) {
                let key = this.pool[i].Name
                this.order[key] = []
            }
            console.log(JSON.stringify(this.order, null, 4))
        },
        methods: {
            shuffle(array) {
                for(let i = array.length - 1; i > 0; i--) {
                    const j = Math.floor(Math.random() * i)
                    const temp = array[i]
                    array[i] = array[j]
                    array[j] = temp
                }
                return array
            },
            choose(prop_listing) {
                const temp = []
                Object.keys(this.order).forEach(key => {
                    let value = this.order[key];
                    for (let j = 0; j < this.prop_listings.length; j++) {
                        // If was chosen or contains the element that was chosen, we want to add all non-chosen elements
                        // to that ordering.
                        if (value.includes(prop_listing.Name) || key == prop_listing.Name) {
                            // Filter the element that was chosen. Filter duplicates.
                            if(this.prop_listings[j] !== prop_listing && !value.includes(this.prop_listings[j].Name)) {
                                value.push(this.prop_listings[j].Name);
                            }
                        }
                    }
                    this.order[key] = value;
                })

                console.log(this.order)
                
                if(this.last) {
                    this.$router.push("evaluation");
                } else {
                    this.prop_listings = this.createListingFromOld();
                }
            },
            createListingFromOld() {
                const empty = []
                Object.keys(this.order).forEach(key => {
                    let value = this.order[key];
                    if (value.length == 0) {
                        empty.push(key)
                    }
                })
                if (empty.length <= 1) {
                    const sorted = this.sortOrder()
                    this.last = true
                    return this.createListingsFromPool(sorted.slice(0, 4));
                } else if (empty.length < 4) {
                    return this.createListingsFromPool(this.shuffle(empty));
                } else {
                    return this.createListingsFromPool(this.shuffle(empty).slice(0,4));
                }
            },
            sortOrder () {
                let array = []
                let result = []
                Object.keys(this.order).forEach(key => {
                    let value = this.order[key];
                    array.push([key, value.length])
                })
                array.sort(function(a, b) {
                    return b[1] - a[1];
                });
                
                for(let i = 0; i < array.length; i++) {
                    result.push(array[i][0]);
                }
                return result
            },
            createListingsFromPool(array) {
                const listings = []
                for (let j = 0; j < this.pool.length; j++) {
                    if (array.includes(this.pool[j].Name)) {
                        listings.push(this.pool[j]);
                    }
                }
                return listings
            }
        },
        props: {
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
