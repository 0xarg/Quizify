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
        <h4 v-if="$store.state.roles =='admin'">
            <p v-if="score>=0" style="color:green">Score: {{ score }}</p>
            <p v-else style="color:red">Not Attempted</p>
        </h4>

        <button v-if="$store.state.roles == 'user'"
            @click="$router.push({ name: 'QuizTake', params: { quiz_id: this.id }, query: { cid: this.chapter_id } })">Take
            Quiz</button>
        <button v-if="$store.state.roles == 'admin'"
            @click="$router.push({ name: 'EditQuiz', params: { quiz_id: this.id }, query: { cid: this.chapter_id } })">Edit
            Quiz</button>
    </div>
</template>

<script>
    export default {
        name: "QuizCard",
        props: ["id","duration","chapter_name","chapter_id","score"]
    }
    


</script>

<style scoped>

</style>