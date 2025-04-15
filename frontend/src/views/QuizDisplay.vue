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
            <button @click="$router.push({name:'EditQuestion',params:{quiz_id: quiz.id, question_id: question.id}})"
                v-if="$store.state.roles == 'admin'">Edit Question ✏️</button>
                <br>
                <br>
            <button v-if="$store.state.roles == 'admin'" style="background-color: lightcoral;"
                @click='DeleteQuestion(question.id)'>delete</button>

        </div>
        <br>
        <button @click="$router.push({name:'AddQuestion',params:{quiz_id: quiz.id}})"
            v-if="$store.state.roles == 'admin'">Add Questions</button>


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
            async DeleteQuestion(question_id) {

                try {
                    const res = await fetch('http://localhost:5000/' + 'api/question/' + question_id, {
                        method: 'DELETE',
                        headers: { 'Content-Type': 'application/json', 'Authentication-Token': JSON.parse(localStorage.getItem('user')).token }
                    })
                    if (res.ok) {
                        alert("Question Deleted")
                        this.$router.push('/Quiz/' + this.cid).then(() => { window.location.reload() })
                    } else {
                        const errorData = await res.json();
                        alert("Error: " + (errorData.message || "Invalid duration format!"));

                    }
                } catch (error) {
                    alert("Error: Could not connect to the server.");
                    console.log(error)
                }
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