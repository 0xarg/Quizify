<template>
    <div>
        <div v-if="!isSubmitted">
            <h1>📝 Take Quiz: {{ quiz_id }}</h1>
            <h3>⏳ Duration: {{ quiz.duration }} minutes</h3>
            <h3>⏳ Total Marks: {{ TotalMarks }} </h3>
            <h3>⏱️ Time Remaining: {{ fTime}}</h3>

            <hr>
        </div>
        <div v-else>
            <h1>🎉 Quiz Completed!</h1>
            <h2>⭐ You scored {{ AcheivedMarks }} out of {{ TotalMarks }}</h2>
            <h2>⭐ Your Quiz Submition Status: {{ status }}</h2>

            <button @click="retakeQuiz">🔄 Retake Quiz</button>
        </div>

        <div v-for="(question,qIndex) in quiz.questions" :key="question.id" class="question-card">
            <h4>Q{{ question.id}}. {{ question.statement }} ({{question.marks}} Mark)</h4>

            <ul>
                <li v-if="!isSubmitted" v-for="(option, index) in question.options" :key="index">
                    <label>
                        <input type="radio" :name="'question-' + qIndex" :value="option"
                            v-model="selectedOptions[qIndex]" />
                        {{ option }}
                    </label>
                </li>
                <li v-if="isSubmitted" v-for="(option, index) in question.options" :key="index" :class="{
                    'correct-answer': option === question.correct_answer,
                    'incorrect-answer': option !== question.correct_answer
                }">
                    {{ option }}
                </li>
            </ul>
            <div v-if="isSubmitted">
                <p v-if="selectedOptions[qIndex] === question.correct_answer" class="correct-answer">Correct</p>
                <p v-else class="incorrect-answer">Incorrect. Correct answer is: {{ question.correct_answer }}</p>
            </div>
        </div>

        <button v-if="!isSubmitted" @click=" submitQuiz">🚀 Submit Quiz</button>
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
            console.log(this.quiz.duration)
            console.log(duration)
            console.log(this.remainingTime)

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
        retakeQuiz(){
            this.isSubmitted = false
            this.AcheivedMarks = 0
            this.selectedOptions= []
            this.remainingTime = this.DuraToMs(this.quiz.duration)
            this.fTime = this.FTime(this.remainingTime)

            clearTimeout(this.autoSub)
            this.autoSub = setTimeout(this.submitQuiz,this.remainingTime);
            clearInterval(this.countdown)
            this.countdown = setInterval(()=> {
                this.remainingTime -= 1000;
                if (this.remainingTime <=0) {
                    this.fTime = "00:00";
                    clearInterval(this.countdown)
                } else {
                    this.fTime = this.FTime(this.remainingTime)
                }
            },1000)

        }
    }

}
</script>

<style scoped>
.question-card {
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 8px;
    margin-bottom: 10px;
}

ul {
    list-style: none;
    padding: 0;
}
.correct-answer {
    color: green;
    font-weight: bold;
}

.incorrect-answer {
    color: red;
}
li {
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 5px;
    cursor: pointer;
    margin-bottom: 5px;
}

li:hover {
    background-color: #f0f0f0;
}

.selected-option {
    background-color: lightblue;
    font-weight: bold;
}

button {
    background-color: green;
    color: white;
    padding: 10px 15px;
    border: none;
    cursor: pointer;
    margin-top: 15px;
}
</style>