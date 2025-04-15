<template>
    <div>
        <h3>Add Chapter</h3>
        <input placeholder="name" v-model="name" />
        <input placeholder="description" v-model="description" />
        <button @click='AddChapter'>Add</button>
    </div>
</template>

<script>
export default {
    name: 'AddChapter',
    props:["id"],
    data() {
        return {
            name: null,
            description: null,
        }
    },
    methods: {
        async AddChapter() {
            const res = await fetch('http://localhost:5000/' + '/api/chapters/'+this.id, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json', 'Authentication-Token': JSON.parse(localStorage.getItem('user')).token }, body: JSON.stringify({ name: this.name, description: this.description })
            })
            if (res.ok) {
                console.log('Valid Chapter')
                const data = await res.json()
                this.$router.push('/Chapters/'+this.id)




            }
        }

    },
    mounted() {
        console.log('Add Subject component mounted');
    },
}
</script>

<style scoped></style>