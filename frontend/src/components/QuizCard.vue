<template>
    <div>
        <hr>
        <h1 @click="$router.push({name:'Quiz', params: {quiz_id: this.id}, query:{cid:this.chapter_id}})"> {{ id }}</h1>
        <h4>{{ duration }}</h4>
        <p>Chapter name: {{ chapter_name }}</p>
        <hr>
    </div>
</template>

<script>
    export default {
        name: "QuizCard",
        props: ["id","duration","chapter_name","chapter_id"]
    }
    


</script>

<style scoped>

</style>