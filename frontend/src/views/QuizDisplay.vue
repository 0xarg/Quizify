<template>
    <div>
        <h1>Quiz:{{ quiz.id }}</h1>
        <h3>Duration for the Quiz: {{ quiz.duration }}</h3>
        <h4>Created on: {{ quiz.date }}</h4>
        <h4>Remarks: {{ quiz.remarks }}</h4>
        <h4>Total Marks: {{ TotalMarks }}</h4>
        <hr>
        <div v-for="question in quiz.questions" :key="question.id">
                <h5>Q{{ question.id }}. {{ question.statement }} ({{ question.marks }} Mark)</h5>
            
            <ol v-if="$store.state.roles =='admin'">
                <li v-for="(option, index) in question.options" :key="index" :class="{ 'correct-answer':option === question.correct_answer,
                           'incorrect-answer':option !== question.correct_answer
                 }">
                    {{ option }}
                </li>
            </ol>
            <ol v-if="$store.state.roles =='user' ">
                <li v-for="(option, index) in question.options" :key="index" :class="{ 'correct-answer':option === question.correct_answer,
                           'incorrect-answer':option !== question.correct_answer
                 }">
                    {{ option }}
                </li>
            </ol>
        </div>
        <button @click="$router.push({name:'AddQuestion',params:{quiz_id: quiz.id}})"
            v-if="$store.state.roles == 'admin'">Add Questions</button>
        <button @click="submitQuiz" v-if="$store.state.roles == 'user'">Submit Quiz</button>


    </div>
</template>

<script>
    export default {
        name: "QuizDisplay",
        props:["quiz_id","cid"],
        data(){
            return{
                quiz:[],
                TotalMarks: 0,
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
                this.calculateTotalMarks()
            }else{
                alert('Chapter not Found')
                this.$router.push('/api/chapters/'+subject_id)
            }

        },
        methods: {
            calculateTotalMarks(){
                this.TotalMarks = this.quiz.questions.reduce((sum,question)=> sum + question.marks,0)
            },
            submitQuiz(){
                
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