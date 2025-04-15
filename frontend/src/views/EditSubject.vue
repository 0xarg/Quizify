<template>
    <div>
        <h3>Edit Subject</h3>
        <br>
        <label for="name">Name:</label>
        <br>
        <input placeholder="name" v-model="name" />
        <br>
        <br>
        <label for="description">Description: </label>
        <br>
        <input placeholder="description" v-model="description" />
        <br>
        <br>
        <button @click='EditSubject'>Edit</button>
    </div>
</template>

<script>
export default {
    name: 'EditSubject',
    props: ['subject_id'],
    data() {
        return {
            name: null,
            description: null,
        }
    },
    methods: {
        async EditSubject() {
            try {
                const res = await fetch('http://localhost:5000/' + 'api/subjects/' + this.subject_id, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json', 'Authentication-Token': JSON.parse(localStorage.getItem('user')).token }, body: JSON.stringify({ name: this.name, description: this.description })
                })
                if (res.ok) {
                    this.$router.push('/subjects')
                } else {
                    const errorData = await res.json();
                    alert("Error: " + (errorData.message || "Invalid Input"));

                }
            } catch (error) {
                alert("Error: Could not connect to the server.");
                console.log(error)
            }
        }

    },

    async mounted() {
        try {
            const res1 = await fetch('http://localhost:5000/' + 'api/subjects/' + this.subject_id, {
                method: 'GET',
                headers: { 'Content-Type': 'application/json', 'Authentication-Token': JSON.parse(localStorage.getItem('user')).token }
            })
            if (res1.ok) {
                const subject = await res1.json()
                this.name = subject.name;
                this.description = subject.description;

            }
        } catch (error) {
            alert("Error: Could not connect to the server.");
            console.log(error)
        }

    },
}
</script>

<style scoped></style>