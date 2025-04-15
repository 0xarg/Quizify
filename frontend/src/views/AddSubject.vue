<template>
    <div>
        <h3>Add Subject</h3>
        <input placeholder="name" v-model="name" />
        <input placeholder="description" v-model="description" />
        <button @click='AddSubject'>Add</button>
    </div>
</template>

<script>
export default {
    name: 'add-subject',
    data() {
        return {
            name: null,
            description: null,
        }
    },
    methods: {
        async AddSubject() {
            const res = await fetch('http://localhost:5000/' + '/api/subjects', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json', 'Authentication-Token': JSON.parse(localStorage.getItem('user')).token }, body: JSON.stringify({ name: this.name, description: this.description })
            })
            if (res.ok) {
                this.$router.push('/subjects')




            }
        }

    },
    mounted() {
        console.log('Add Subject component mounted');
    },
}
</script>

<style scoped></style>