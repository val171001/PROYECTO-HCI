<template>
    <div>
        <qrcode-stream @decode="onDecode"></qrcode-stream>
        <q-page-sticky position="bottom-right" :offset="[18, 18]">
            <q-btn fab icon="arrow_back" color="primary" @click="main"/>
        </q-page-sticky>
    </div>
</template>
<script>
import router from '@/router'
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
            this.validate()
        },
        validate(){
            let success = this.response[0].added
            if (success) {
                this.$q.notify({message: 'Puntos agregados exitosamente!'})
                router.push({name: 'Home'})
            } else {
                this.$q.notify({ color: 'negative', message: 'Codigo no valido', icon: 'report_problem' })
            }
        },
        main() {
            router.push({name: 'Home'})
        }
    }
}
</script>
