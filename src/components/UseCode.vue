<template>
    <div>
        <q-btn label="Comprar" @click="buy"/>
    </div>
</template>

<script>
export default {
    name: 'UsePoints',
    props: ["userid", "code"],
    methods: {
        async buy(){
            console.log(this.userid, this.code)
            const post = this.$http.post
            await post(
                '/client/user/get/code',
                {
                    userId: this.userid,
                    code: this.code
                }
            ).then(results => {
                console.log(results)
            }).catch(error => {
                console.log(error)
            })
        }
    }
}
</script>

