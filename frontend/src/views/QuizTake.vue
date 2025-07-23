<template>
 
    <div class="quiz-wrapper">
        <div v-if="!isSubmitted">
            <section class="quiz-info-card">
                <h2>📖 Quiz: {{ quiz_id }}</h2>
                <p>Duration: {{ quiz.duration }}</p>
                <p>Total Marks: {{ TotalMarks }}</p>
                <p>Duration: {{ quiz.duration }}</p>

            </section>
            <section  class=" quiz-info-card-buttons button-section">
                <div class="timer">
                    <h5>{{ fTime }}</h5>
                </div>
                <div class="button-section">
                    <button class="test-sbmt" @click="submitQuiz">Sumbit</button>
                </div>
            </section>
        </div>
        <div v-if="isSubmitted">
            <section class="quiz-info-card">
                <h3>🎉 Quiz Completed!</h3>
                <p>⭐ You scored {{ AcheivedMarks }} out of {{ TotalMarks }}</p>
                <p>📋 Submission Status: {{ status }}</p>
            </section>
            <section class=" quiz-info-card-buttons button-section">
                <button class="test-sbmt" @click="exitExam">Back to All Quizes</button>
            </section>
        </div>

        <main class="quiz-body">

            <section class="quiz-question" v-for="(question, qIndex) in quiz.questions" :key="question.id">
                Q{{ question.id }}. {{ question.statement }} ({{ question.marks }} Mark)
                <form class="options">
                    <label v-for="(option, oIndex) in question.options" :key="oIndex"><input type="radio" name="q1"
                            :name="'question-' + qIndex" :value="option" v-model="selectedOptions[qIndex]" />  {{ option
                        }}</label>
                </form>
            </section>


        </main>

    </div>
</template>

<script>
export default {
    name: "QuizTake",
    props: ["quiz_id", "cid"],
    data() {
        return {
            quiz: [],
            selectedOptions: [],
            TotalMarks: 0,
            AcheivedMarks: 0,
            isSubmitted: false,
            status: null,
            remainingTime: 0,
            fTime: '',
            autoSub: null,
            countdown: null,
        }
    },
    async mounted() {
        const res = await fetch('http://localhost:5000/' + '/api/quiz/' + this.quiz_id, {
            headers: {
                'Authentication-Token': JSON.parse(localStorage.getItem('user')).token
            }
        })
        if (res.ok) {
            this.quiz = await res.json()
            this.calculateTotalMarks()
            const duration = this.DuraToMs(this.quiz.duration);
            this.remainingTime = duration
            this.fTime = this.FTime(this.remainingTime)

            this.autoSub = setTimeout(this.submitQuiz, duration)

            this.countdown = setInterval(()=> {
                this.remainingTime -= 1000;
                if (this.remainingTime <=0) {
                    this.fTime = "00:00";
                    clearInterval(this.countdown)
                } else {
                    this.fTime = this.FTime(this.remainingTime)
                }
            },1000)


        } else {
            alert('Chapter not Found')
            this.$router.push('/api/chapters/' + subject_id)
        }

    },
    methods: {
        calculateTotalMarks() {
            this.TotalMarks = this.quiz.questions.reduce((sum, question) => sum + question.marks, 0)
        },

        DuraToMs(duration){
            const [h, m, s] = duration.split(':').map(Number)
            return(
               (h*3600 + m*60 + s)*1000
            );
        },

        FTime(ms) {
            const totalS = Math.floor(ms/1000);
            const mins = String(Math.floor(totalS/60)).padStart(2,'0');
            const sec = String(totalS % 60).padStart(2,'0');
            return `${mins}min:${sec}sec`;
        },


        exitExam(){
            this.$router.push(`/Quizes/${this.cid}`)
        },
        async submitQuiz() {
            let scored = 0;
            clearTimeout(this.autoSub)
            clearInterval(this.countdown)

            this.isSubmitted = true

            this.quiz.questions.forEach((question,index)=>{
                if (this.selectedOptions[index] == question.correct_answer){
                    scored += question.marks
                }
            });
            this.AcheivedMarks = scored;

            try {
                const res = await fetch('http://localhost:5000/' + 'api/SubmitQuiz/' + this.quiz_id, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authentication-Token': JSON.parse(localStorage.getItem('user')).token
                    },
                    body: JSON.stringify({ total_score: this.AcheivedMarks, duration: this.duration })
                })
                if (res.ok) {
                    this.status = 'Successfully Submitted'
                } else {
                    this.status = 'There is an error in your submition, Please contact support team '

                }
            } catch (error) {
                alert("Error: Could not connect to the server.");
                console.log(error)
            }

        },
    }

}
</script>

<style scoped></style>