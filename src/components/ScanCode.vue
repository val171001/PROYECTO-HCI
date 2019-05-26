<template>
    <div>
        <qrcode-stream @decode="onDecode"></qrcode-stream>
        <span>
            {{response}}
        </span>
    </div>
</template>
<script>
export default {
    name: 'ScanCode',
    data(){
        return {
            code: '',
            response: null
        }
    },
    methods: {
        onDecode(decodedString) {
            console.log(decodedString)
            this.code = decodedString
            this.afterScan()
        },
        async afterScan() {
            this.$q.loading.show({ delay: 400 })
            const get = this.$http.get
            const email = this.$user.email
            const code = this.code
            await get(
                '/client/scan',
                {
                    params: {
                        email: email,
                        code: code  
                    }
                }
            ).then( res => {
                this.response = res.data
            }).catch(error => {
                console.log(error)
            })
            this.$q.loading.hide()
        }
    }
}
</script>

