<template>
    <div id="adminMain">
        <div class="sidebar">
            <div class="dash-logo"></div>
            <ul class="menu">
                <li class="active">
                    <a href="/brand_home">
                        <i class="fas fa-tachometer-alt"></i>
                        <span>Dashboard</span>
                    </a>
                </li>
                <li>
                    <a :href="`/brand_profile/${sid}`">
                        <i class="fas fa-user"></i>
                        <span>Profile</span>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <i class="fas fa-chart-bar"></i>
                        <span>Statistics</span>
                    </a>
                </li>
                <li>
                    <a href="/new_camp">
                        <i class="fa-solid fa-snowflake"></i>
                        <span>Campaign</span>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <i class="fas fa-cog"></i>
                        <span>Settings</span>
                    </a>
                </li>
                <li class="logout">
                    <a href="/brand_login">
                        <i class="fas fa-sign-out-alt"></i>
                        <span>Log Out</span>
                    </a>
                </li>
            </ul>
        </div>

        <div class="content-area-adminQuiz">
            <div id="sidebar-AdminQuiz">
                <div id="desc-AdminQuiz">
                    <h2>Exam: </h2>
                    <h2>Quiz-{{ quiz.id }}</h2>
                    <h6>Chapter :</h6>
                    <h6>{{ cname }}</h6>
                    <h6>Duration : </h6>
                    <h6>{{ quiz.duration }} (HH:MM:SS)</h6>
                    <h6>Remarks :</h6>
                    <h6>{{ quiz.remarks }}</h6>
                    <h6>Total Marks :</h6>
                    <h6>{{ totalMarks }}</h6>
                </div>
                <hr>
            </div>

            <div id="quiz-AdminQuiz">
                <div id="ques-box-AdminQuiz" v-for="question in quiz.questions" :key="question.id">
                    <h5>Q{{ question.id }}. {{ question.statement }} ({{ question.marks }} Mark)</h5>

                    <ol>
                        <li v-for="(option, index) in question.options" :key="index" :class="{
                            'correct-answer': option === question.correct_answer,
                            'incorrect-answer': option !== question.correct_answer
                        }">
                            {{ option }}
                        </li>
                    </ol>
                    <div id="ques-btns">

                        <button class="abtn" style="width:80px;" data-bs-toggle="modal" data-bs-target="#changeModal"
                            @click="changeInit(question)">Edit
                        </button>
                        <button @click="deleteQues(question.id)" class="abtn" id="delbtn"
                            style="width: 100px; margin: 0px 0px">delete</button>
                    </div>
                    <hr style="width:500px;">
                </div>

                <div id="addQues">
                    <button style="margin-bottom: 50px;" class="abtn" data-bs-toggle="modal"
                        data-bs-target="#exampleModal">Add
                    </button>
                </div>

            </div>
        </div>
    </div>


    <!-- 
    <div>
        <div id="sidebar-AdminQuiz">
            <div id="desc-AdminQuiz">
                <h2>Exam: </h2>
                <h2>Quiz-{{ quiz.id }}</h2>
                <h6>Chapter :</h6>
                <h6>{{ cname }}</h6>
                <h6>Duration : </h6>
                <h6>{{ quiz.duration }} (HH:MM:SS)</h6>
                <h6>Remarks :</h6>
                <h6>{{ quiz.remarks }}</h6>
                <h6>Total Marks :</h6>
                <h6>{{ totalMarks }}</h6>
            </div>
            <hr>
        </div>

        <div class="sidebar">
            <div class="dash-logo"></div>
            <ul class="menu">
                <li class="active">
                    <a href="/brand_home">
                        <i class="fas fa-tachometer-alt"></i>
                        <span>Dashboard</span>
                    </a>
                </li>
                <li>
                    <a :href="`/brand_profile/${sid}`">
                        <i class="fas fa-user"></i>
                        <span>Profile</span>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <i class="fas fa-chart-bar"></i>
                        <span>Statistics</span>
                    </a>
                </li>
                <li>
                    <a href="/new_camp">
                        <i class="fa-solid fa-snowflake"></i>
                        <span>Campaign</span>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <i class="fas fa-cog"></i>
                        <span>Settings</span>
                    </a>
                </li>
                <li class="logout">
                    <a href="/brand_login">
                        <i class="fas fa-sign-out-alt"></i>
                        <span>Log Out</span>
                    </a>
                </li>
            </ul>
        </div>
        <div id="quiz-AdminQuiz">
            <div id="ques-box-AdminQuiz" v-for="question in quiz.questions" :key="question.id">
                <h5>Q{{ question.id }}. {{ question.statement }} ({{ question.marks }} Mark)</h5>

                <ol>
                    <li v-for="(option, index) in question.options" :key="index" :class="{
                        'correct-answer': option === question.correct_answer,
                        'incorrect-answer': option !== question.correct_answer
                    }">
                        {{ option }}
                    </li>
                </ol>
                <div id="ques-btns">

                    <button class="abtn" style="width:80px;" data-bs-toggle="modal" data-bs-target="#changeModal"
                        @click="changeInit(question)">Edit
                    </button>
                    <button @click="deleteQues(question.id)" class="abtn" id="delbtn"
                        style="width: 100px; margin: 0px 0px">delete</button>
                </div>
                <hr>
            </div>

            <div id="addQues">
                <button style="margin-bottom: 50px;" class="abtn" data-bs-toggle="modal"
                    data-bs-target="#exampleModal">Add
                </button>
            </div>

        </div>
    </div> -->
    <!-- <div id="top-container-AdminQuiz">
        

        <div id="sidebar-AdminQuiz">
            <div id="desc-AdminQuiz">
                <h2>Exam: </h2>
                <h2>Quiz-{{ quiz.id }}</h2>
                <h6>Chapter :</h6>
                <h6>{{ cname }}</h6>
                <h6>Duration : </h6>
                <h6>{{ quiz.duration }} (HH:MM:SS)</h6>
                <h6>Remarks :</h6>
                <h6>{{ quiz.remarks }}</h6>
                <h6>Total Marks :</h6>
                <h6>{{ totalMarks }}</h6>
            </div>
            <hr>
        </div>
        <div class="divider-AdminQuiz"></div>
        <div id="quiz-AdminQuiz">
            <div id="ques-box-AdminQuiz" v-for="question in quiz.questions" :key="question.id">
                <h5>Q{{ question.id }}. {{ question.statement }} ({{ question.marks }} Mark)</h5>

                <ol>
                    <li v-for="(option, index) in question.options" :key="index" :class="{
                        'correct-answer': option === question.correct_answer,
                        'incorrect-answer': option !== question.correct_answer
                    }">
                        {{ option }}
                    </li>
                </ol>
                <div id="ques-btns">

                    <button class="abtn" style="width:80px;" data-bs-toggle="modal" data-bs-target="#changeModal"
                        @click="changeInit(question)">Edit
                    </button>
                    <button @click="deleteQues(question.id)" class="abtn" id="delbtn"
                        style="width: 100px; margin: 0px 0px">delete</button>
                </div>
                <hr>
            </div>

            <div id="addQues">
                <button style="margin-bottom: 50px;" class="abtn" data-bs-toggle="modal"
                    data-bs-target="#exampleModal">Add
                </button>
            </div>

        </div>
    </div> -->


    <!-- Modals -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Add a Question</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="mb-2">
                        <label for="title" class="col-form-label">Statement</label>
                        <input type="text" class="form-control" id="statement" name="title"
                            placeholder="Question Statement" v-model="statement" />
                    </div>
                    <div class="mb-2">
                        <label for="opt1" class="col-form-label">Option 1: </label>
                        <input type="text" class="form-control" id="opt1" name="opt1" v-model="option_1"
                            placeholder="Option 1">
                    </div>
                    <div class="mb-2">
                        <label for="opt2" class="col-form-label">Option 2: </label>
                        <input type="text" class="form-control" id="opt2" name="opt2" v-model="option_2"
                            placeholder="Option 2">
                    </div>
                    <div class="mb-2">
                        <label for="opt3" class="col-form-label">Option 3: </label>
                        <input type="text" class="form-control" id="opt3" name="opt3" v-model="option_3"
                            placeholder="Option 3">
                    </div>
                    <div class="mb-2">
                        <label for="opt4" class="col-form-label">Option 4: </label>
                        <input type="text" class="form-control" id="opt4" name="opt4" v-model="option_4"
                            placeholder="Option 4">
                    </div>
                    <div class="mb-2">
                        <label for="marks" class="col-form-label">Marks: </label>
                        <input type="number" class="form-control" id="marks" name="marks" v-model="marks"
                            placeholder="Marks">
                    </div>
                    <label for="correct_answer" class="col-form-label">Correct Option: </label>
                    <select name="correct_answer" v-model="correct_answer" required class="form-select"
                        aria-label="Default select example">
                        <option :value="option_1">{{ option_1 || "Option 1" }}</option>
                        <option :value="option_2">{{ option_2 || "Option 2" }}</option>
                        <option :value="option_3">{{ option_3 || "Option 3" }}</option>
                        <option :value="option_4">{{ option_4 || "Option 4" }}</option>
                    </select>
                    <hr>

                    <button type="submit" id="sbmt-btn" class="btn btn-outline-dark" @click="AddQuestion()">Add
                        Question</button>
                    <button type="button" class="btn btn-outline-secondary" data-bs-dismiss="modal" hidden></button>
                </div>
                <div class="modal-footer"></div>
            </div>
        </div>
    </div>

    <div class="modal fade" id="changeModal" tabindex="-1" aria-labelledby="exampleModalLabel1" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel1">Edit Question</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="mb-2">
                        <label for="title" class="col-form-label">Statement</label>
                        <input type="text" class="form-control" id="statement" name="title" v-model="statement" />
                    </div>
                    <div class="mb-2">
                        <label for="opt1" class="col-form-label">Option 1: </label>
                        <input type="text" class="form-control" id="opt1" name="opt1" v-model="option_1"
                            placeholder="Option 1">
                    </div>
                    <div class="mb-2">
                        <label for="opt2" class="col-form-label">Option 2: </label>
                        <input type="text" class="form-control" id="opt2" name="opt2" v-model="option_2"
                            placeholder="Option 2">
                    </div>
                    <div class="mb-2">
                        <label for="opt3" class="col-form-label">Option 3: </label>
                        <input type="text" class="form-control" id="opt3" name="opt3" v-model="option_3"
                            placeholder="Option 3">
                    </div>
                    <div class="mb-2">
                        <label for="opt4" class="col-form-label">Option 4: </label>
                        <input type="text" class="form-control" id="opt4" name="opt4" v-model="option_4"
                            placeholder="Option 4">
                    </div>
                    <div class="mb-2">
                        <label for="marks" class="col-form-label">Marks: </label>
                        <input type="number" class="form-control" id="marks" name="marks" v-model="marks"
                            placeholder="Marks">
                    </div>
                    <label for="correct_answer" class="col-form-label">Correct Option: </label>
                    <select name="correct_answer" v-model="correct_answer" required class="form-select"
                        aria-label="Default select example">
                        <option :value="option_1">{{ option_1 || "Option 1" }}</option>
                        <option :value="option_2">{{ option_2 || "Option 2" }}</option>
                        <option :value="option_3">{{ option_3 || "Option 3" }}</option>
                        <option :value="option_4">{{ option_4 || "Option 4" }}</option>
                    </select>
                    <hr>
                    <button type="submit" id="sbmt-btn" class="btn btn-outline-dark"
                        @click="editQuestion(this.question_id)">Save
                        Changes</button>
                    <button type="button" class="btn btn-outline-secondary" data-bs-dismiss="modal" hidden></button>
                </div>
                <div class="modal-footer"></div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "AdminQuiz",
        props:["quiz_id","remarks","cid","cname","tques"],
        data(){
            return{
                quiz:[],
                totalMarks: 0,
                statement: null,
                option_1: null,
                option_2: null,
                option_3: null,
                option_4: null,
                correct_answer: null,
                marks: null,
                question_id:null
            }
        },
        methods:{

            calculateTotalMarks() {
                this.totalMarks = this.quiz.questions.reduce((sum, question) => sum + question.marks, 0)
            },
            async fetchQuiz(){
                try {
                    const res = await fetch('http://localhost:5000/' + 'api/quiz/' + this.quiz_id, {
                        headers: {
                            'Authentication-Token': JSON.parse(localStorage.getItem('user')).token
                        }
                    })
                    if (res.ok) {
                        this.quiz = await res.json()
                        this.calculateTotalMarks()
                    }
                } catch (error) {
                    console.error(error);
                }
            },

            async AddQuestion(){
                try {
                    const res = await fetch('http://localhost:5000/' + 'api/add/question/' + this.quiz_id, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json', 'Authentication-Token': JSON.parse(localStorage.getItem('user')).token },
                        body: JSON.stringify({ statement: this.statement, option_1: this.option_1, option_2: this.option_2, option_3: this.option_3, option_4: this.option_4, correct_answer: this.correct_answer, marks: this.marks })
                    })
                    if (res.ok) {
                        document.querySelector('#exampleModal .btn-close').click();
                        this.statement= null,
                        this.option_1= null,
                        this.option_2= null,
                        this.option_3= null,
                        this.option_4= null,
                        this.correct_answer= null,
                        this.marks= null,
                        await this.fetchQuiz()
                    }
                } catch (error) {
                    console.error(error)
                }
            },
            async changeInit(question) {
                this.question_id = question.id;
                this.statement = question.statement,
                this.option_1 = question.options[0],
                this.option_2 = question.options[1]
                this.option_3 = question.options[2]
                this.option_4 = question.options[3]
                this.correct_answer = question.correct_answer,
                this.marks = question.marks
                
            },
            async editQuestion(question_id) {
                try {
                    const res = await fetch('http://localhost:5000/' + 'api/question/' + question_id, {
                        method: 'PUT',
                        headers: { 'Content-Type': 'application/json', 'Authentication-Token': JSON.parse(localStorage.getItem('user')).token },
                        body: JSON.stringify({ statement: this.statement, option_1: this.option_1, option_2: this.option_2, option_3: this.option_3, option_4: this.option_4, correct_answer: this.correct_answer, marks: this.marks })
                    })
                    if (res.ok) {
                        document.querySelector('#changeModal .btn-close').click();
                        this.statement = null,
                        this.option_1 = null,
                        this.option_2 = null,
                        this.option_3 = null,
                        this.option_4 = null,
                        this.correct_answer = null,
                        this.marks = null,
                        this.question_id = null
                        await this.fetchQuiz()

                    }
                } catch (error) {
                    console.error(error)
                }
            },

            async deleteQues(question_id){
                try {
                    const res = await fetch('http://localhost:5000/' + 'api/question/' + question_id, {
                        method: 'DELETE',
                        headers: { 'Content-Type': 'application/json', 'Authentication-Token': JSON.parse(localStorage.getItem('user')).token }
                    })
                    if (res.ok) {
                        await this.fetchQuiz();
                    } 
                } catch (error) {
                    console.error(error)
                }
            },
        },

        mounted(){
            this.fetchQuiz();
        }


    }
</script>

<style scoped>

</style>