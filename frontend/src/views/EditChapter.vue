<template>
    <div>
        <h3>Edit Chapter</h3>
        <label for="name">Name of the Chapter</label>
        <input placeholder="name" v-model="name" id="name" />
        <br>
        <br>
        <label for="description">Description</label>
        <input placeholder="description" id="description" v-model="description" />
        <br>
        <br>
        <button @click='EditChapter'>Edit</button>
    </div>
</template> 

<script>
export default {
    name: 'EditChapter',
    props: ["chapter_id"],
    data() {
        return {
            name: null,
            description: null,
        }
    },
    methods: {
        async EditChapter() {
            try {
                const res = await fetch('http://localhost:5000/' + 'api/chapter/' + this.chapter_id, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json', 'Authentication-Token': JSON.parse(localStorage.getItem('user')).token }, body: JSON.stringify({ name: this.name, description: this.description })
                })
                if (res.ok) {
                    this.$router.push('/Chapters/' + this.chapter_id)
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
            const res1 = await fetch('http://localhost:5000/' + 'api/chapter/' + this.chapter_id, {
                method: 'GET',
                headers: { 'Content-Type': 'application/json', 'Authentication-Token': JSON.parse(localStorage.getItem('user')).token }
            })
            if (res1.ok) {
                const chapter = await res1.json()
                this.name = chapter.name;
                this.description = chapter.description;

            }
        } catch (error) {
            alert("Error: Could not connect to the server.");
            console.log(error)
        }

    },

}
</script>

<style scoped></style>