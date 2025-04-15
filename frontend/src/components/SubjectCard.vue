<template>
    <div>

        <div class="subject">
            <h2 @click="$router.push('/Subject/' + subject_id)" class="clickable">{{ name }}</h2>
            <p><strong>Description:</strong> {{ description }}</p>
            <p><strong>Subject ID:</strong> {{ subject_id }}</p>
            <button v-if="$store.state.roles == 'admin'"
                @click="$router.push({ name: 'EditSubject', params: { subject_id: this.subject_id } })">Edit
                Subject</button>
                <br>
            <button style="background-color: lightcoral;" @click='DeleteSubject'>delete</button>

            <hr>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'SubjectCard',
        props: ["name","description","subject_id"],
        methods: {
            async DeleteSubject() {
                const res = await fetch('http://localhost:5000/' + '/api/subjects/' + this.subject_id, {
                    method: 'DELETE',
                    headers: { 'Content-Type': 'application/json', 'Authentication-Token': JSON.parse(localStorage.getItem('user')).token }, body: JSON.stringify({ name: this.name, description: this.description })
                })
                if (res.ok) {
                    alert("Subject Deleted")
                    this.$router.push( '/subjects').then(()=> {window.location.reload()})

                    




                }
            }

        },
    }
</script>

<style scoped>

/* GPT Generated CSS */
.clickable {
    cursor: pointer;
    color: rgb(255, 72, 0);
    text-decoration: underline;
}

.clickable:hover {
    color: darkblue;
}

.subject {
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 8px;
    margin-bottom: 10px;
}

button {
    background-color: green;
    color: white;
    padding: 8px 15px;
    border: none;
    cursor: pointer;
    margin-bottom: 15px;
}
</style>