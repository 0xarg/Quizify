<template>
    <div>
        <h1>Quiz:{{ quiz.id }}</h1>
        <h3>Duration for the Quiz: {{ quiz.duration }}</h3>
        <h4>Created on: {{ quiz.date }}</h4>
        <h4>Remarks: {{ quiz.remarks }}</h4>
        <hr>
        <div v-for="question in quiz.questions" :key="question.id">
            <h5>Q{{ question.id }}. {{ question.statement }}</h5>
            <ol>
                <li v-for="(option, index) in question.options" :key="index" :class="{ 'correct-answer':option === question.correct_answer,
                           'incorrect-answer':option !== question.correct_answer
                 }">
                    {{ option }}
                </li>
            </ol>
        </div>
        <button @click="$router.push({name:'AddQuestion',params:{quiz_id: quiz.id}})">Add Questions</button>


    </div>
</template>

<script>
    export default {
        name: "QuizDisplay",
        props:["quiz_id","cid"],
        data(){
            return{
                quiz:[]
            }
        },
        async mounted(){
            const res = await fetch('http://localhost:5000/' + '/api/quiz/' + this.quiz_id,{
                headers: {
                    'Authentication-Token': JSON.parse(localStorage.getItem('user')).token
                }
            })
            if (res.ok){
                this.quiz = await res.json()
            }else{
                alert('Chapter not Found')
                this.$router.push('/api/chapters/'+subject_id)
            }

        }

    }
</script>

<style scoped>
.correct-answer {
    color: green;
    font-weight: bold;
}
.incorrect-answer {
    color: red;
}


</style>