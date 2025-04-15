<template>
    <div>
        <hr>
        <h1 v-if="$store.state.roles =='admin'"
            @click="$router.push({name:'Quiz', params: {quiz_id: this.id}, query:{cid:this.chapter_id}})"> {{ id }}</h1>
        <h3 v-if="$store.state.roles =='user'"> Quiz {{ id }}</h3>
        <h4>{{ duration }}</h4>
        <p>Chapter name: {{ chapter_name }}</p>
        <h4 v-if="$store.state.roles =='user'">
            <p v-if="score>=0" style="color:green">Score: {{ score }}</p>
            <p v-else style="color:red">Not Attempted</p>
        </h4>
        <!-- <h4 v-if="$store.state.roles =='admin'">
            <p v-if="score>=0" style="color:green">Score: {{ score }}</p>
            <p v-else style="color:red">Not Attempted</p>
        </h4> -->

        <button v-if="$store.state.roles == 'user'"
            @click="$router.push({ name: 'QuizTake', params: { quiz_id: this.id }, query: { cid: this.chapter_id } })">Take
            Quiz</button>
        <button v-if="$store.state.roles == 'admin'"
            @click="$router.push({ name: 'EditQuiz', params: { quiz_id: this.id }, query: { cid: this.chapter_id } })">Edit
            Quiz</button>
        <button v-if="$store.state.roles == 'admin'" style="background-color: lightcoral;" @click='DeleteQuiz'>delete</button>

    </div>
</template>

<script>
    export default {
        name: "QuizCard",
        props: ["id","duration","chapter_name","chapter_id","score"],
        methods: {
                    async DeleteQuiz() {
                    
                    try {
                        const res = await fetch('http://localhost:5000/' + '/api/quiz/' + this.id, {
                            method: 'DELETE',
                            headers: { 'Content-Type': 'application/json', 'Authentication-Token': JSON.parse(localStorage.getItem('user')).token }
                        })
                        if (res.ok) {
                            alert("Quiz Deleted")
                            this.$router.push('/Quizes/'+this.chapter_id).then(() => { window.location.reload() })
                        } else {
                            const errorData = await res.json();
                            alert("Error: " + (errorData.message || "Invalid duration format!"));

                        }
                    } catch (error) {
                        alert("Error: Could not connect to the server.");
                        console.log(error)
                    }
            }
    
        },
    }
    


</script>

<style scoped>

</style>