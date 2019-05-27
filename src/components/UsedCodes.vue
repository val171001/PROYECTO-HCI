<template>
    <div class="q-pa-md row items-start q-gutter-md">
        <q-card v-for="code in codes" v-bind:key="code.codigo">
            <q-card-section>
                <div class="text-h6">{{code.codigo}}</div>
            </q-card-section>
            <q-card-section>
                <div class="text-h6">{{code.valorcodigo}}</div>
            </q-card-section>
            <q-card-section>
                <div class="text-h6">{{code.marca}}</div>
            </q-card-section>
        </q-card>
    </div>



</template>

<script>
export default {
    name: 'UsedCodes',
    data() {
        return {
            codes: []
        }
    },
    mounted(){
        this.getCodes()
    },
    methods: {
        async getCodes(){
            const get = this.$http.get
            const id = this.$user.id
            await get(
                '/client/user/get/code/used',
                {
                    params: {
                        userId: id
                    }
                }
            ).then(res => {
                this.codes = res.data
            }).catch(error => {
                console.log(error)
            })
        }
    }
}
</script>
