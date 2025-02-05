<template>
    <div>
        <h1>{{ chapter.name }}</h1>
        <h3>{{ chapter.description }}</h3>
        <h4> Chapter_id: {{ chapter_id }}</h4>
        <h4>Subject_id: {{ sid }}</h4>
        <a href="">
            <h5 @click="$router.push({name:'QuizList', params: {chapter_id: this.chapter_id}})">View Quizes</h5>
            <!-- <h5   v-if="$store.state.roles == 'user'" @click="$router.push({name:'QuizList', params: {chapter_id: this.chapter_id}})">View & Take Quizes</h5> -->
        </a>
        <button @click="$router.push({name:'AddQuiz', params: {chapter_id: this.chapter_id}, query:{sid:this.sid}})"
            v-if="$store.state.roles =='admin'"> Add Quiz</button>

    </div>
</template>

<script>
    export default {
        name: "ChapterDisplay",
        props:["sid","chapter_id"],
        data(){
            return{
                chapter:[]
            }
        },
        async mounted(){
            const res = await fetch('http://localhost:5000/' + '/api/chapter/' + this.chapter_id,{
                headers: {
                    'Authentication-Token': JSON.parse(localStorage.getItem('user')).token
                }
            })
            if (res.ok){
                this.chapter = await res.json()
            }else{
                alert('Chapter not Found')
                this.$router.push('/api/chapters/'+subject_id)
            }

        }

    }
</script>

<style scoped>

</style>