<template>
    <div>
        <qrcode-stream @decode="onDecode"></qrcode-stream>
        <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Cum ut magni, dignissimos temporibus mollitia libero accusamus, reiciendis esse atque nobis a reprehenderit quos, fuga iste. Accusantium iure animi nemo mollitia.
        </p>
    </div>
</template>
<script>
export default {
    name: 'ScanCode',
    methods: {
        onDecode(decodedString) {
            console.log(decodedString)
        }
    }
}
</script>

