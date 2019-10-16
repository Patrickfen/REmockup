<template>
    <div>
        <div> 
            <b-alert class="alert" show>  
                <b-row class="text-c">
                    <h3 class="text-c help-text">Please choose the listing you find the most trustworthy. ({{actions}} / {{total}})</h3>
                </b-row>
                <b-row class=""  v-if="biased">
                    <b-spinner class="spinner-center" style="width: 3rem; height: 3rem;" label="Large Spinner"></b-spinner>
                </b-row>
            </b-alert>
        </div>
        <b-row>
            <b-col class="no-padding">  
                <b-row class="no-r-margin" if="pool">
                    <listing class="listing col-md-6" v-for="prop_listing in prop_listings" :prop_listing="prop_listing" :key="prop_listing.Name">
                    </listing>
                </b-row>
            </b-col>
            <b-col v-if="biased" md="2">
                <b-row>
                    <div class="addtext">Advertisement</div>
                    <b-img fluid :src="require('../assets/lock-eye.png')"></b-img>
                    <div class="add"></div>
                </b-row>

            </b-col>
        </b-row>
    </div>
</template>

<script>
import listing from "../components/Listing.vue"
import dataset from "@/assets/dataset.json"
import bad_dataset from "@/assets/datasetbad.json"
    export default {
        name: 'listings',
        data() {
            return {
                last : false,
                prop_listings : [],
                order : {},
                biased: null,
                pool : dataset,
                timestamps : [],
                actions: 0,
                total: 0
            }
        },
        mounted() {
            this.biased = ((Math.random() > 0.5) ? true : false)
            this.prop_listings = this.shuffle(this.pool).slice(0,4);
            for (let i = 0; i < this.pool.length; i++) {
                let key = this.pool[i].Name
                this.order[key] = []
            }
            console.log(JSON.stringify(this.order, null, 4))
            this.total = this.pool.length;

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
                const temp = [];
                var currentdate = new Date(); 
                var dtString = "" + currentdate.getDate() + "/"
                                + (currentdate.getMonth()+1)  + "/" 
                                + currentdate.getFullYear() + " "  
                                + currentdate.getHours() + ":"  
                                + currentdate.getMinutes() + ":" 
                                + currentdate.getSeconds();
                this.timestamps.push(dtString);
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
                    const resultSet = {
                        "order" : this.order,
                        "timestamps" : this.timestamps,
                        "biased" : this.biased
                    }
                    var ctx = this;
                    this.axios.post('/api', resultSet)
                    .then(function(){
                        ctx.$router.push("evaluation");
                    })
                    .catch(function(e){
                        alert('Something went wrong');
                        console.log(e);
                    })
                } else {
                    this.prop_listings = this.createListingFromOld();
                }
                
                this.actions += 1
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
    .listing {
        // height: 45%;
        // max-height: 45vh;
        // height: 50vh;
        
        // overflow: visible;
    }

    @media only screen and (max-width: 600px) {
        .listing {
            max-height: 1000px;
        }
    }


    .help-text {
        text-align: center;
    }

    .no-r-margin {
        margin-right: 0;
    }

    .alert {
        margin-bottom: 0px !important;
        text-align: center;
    }

    .add {
        background-image: url('../assets/lock-ad.png');
        background-position: center;
        background-size: cover;
        width: 100%;
        height: 500px;
    }
    
    .addtext {
        color: #665;
        text-align: right;
        display: inline-block;
        padding-right: 20px;
    }

    .no-padding {
        padding-right: 0px;
    }

    .text-c {
        text-align: center;
        width: 100%;
    }

    .spinner-center {
        margin: auto;
    }
</style>
