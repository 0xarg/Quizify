<template>
    <div class="dash-camp-body">
        <Sidebar />

        <div class="main--content">
            <Topbar :pname="cname" :count="tquiz"/>

            <div class="card--container">
                <h3 class="main--title">Quizes</h3>
                <div class="card--wrapper">
                    <div v-for="quiz in quizes" :key="quiz.id" class="camp--card">
                        <div class="card--header">
                            <div class="amount">
                                <span class="title">Quiz-{{ quiz.id }}</span>
                                <span class="amount--value-camp"></span>
                                <span class="card--detail">{{ quiz.remarks }}</span>
                                <br>
                                <span class="card--detail">{{ quiz.duration }}</span>
                            </div>
                            <i class="fa-brands fa-canadian-maple-leaf"></i>
                        </div>
                        <div>
                            <button class="abtn" style="width: 100px" data-bs-toggle="modal"
                                data-bs-target="#changeModal" v-if="$store.state.roles == 'admin'"
                                @click="changeInit(quiz)">Change</button>
                        </div>
                        <div>
                            <button type="submit" @click="deleteQuiz(quiz.id)" class="abtn" id="delbtn"
                                style="width: 100px; margin: 10px 0px" v-if="$store.state.roles == 'admin'">
                                Delete
                            </button>
                        </div>
                        <div>
                            <button v-if="$store.state.roles == 'admin'"  class="abtn" style="text-decoration: none; color: chocolate;"
                                @click="$router.push({ name: 'Quiz', params: { quiz_id: quiz.id }, query: { remarks: quiz.remarks, totalQues: quiz.questions.length, chapter_id: cid, chapter_name: cname} })">
                                View More
                            </button>
                            <button  v-if="$store.state.roles == 'user'" class="abtn" style="text-decoration: none; color: chocolate;"
                                @click="$router.push({ name: 'QuizTake', params: { quiz_id: quiz.id }, query: { chapter_id: cid} })">
                                Take Quiz
                            </button>
                        </div>
                    </div>

                    <div class="add-camp--card" v-if="$store.state.roles == 'admin'">
                        <div class="card--header">
                            <div class="amount">
                                <span class="title"></span>
                                <span class="add-camp">
                                    <a href="" class="icon-add" data-bs-toggle="modal" data-bs-target="#exampleModal">
                                        <i class="fa-solid fa-plus"></i>
                                    </a>
                                </span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- MODAL -->
        <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="exampleModalLabel">Add a Quiz</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="mb-2">
                            <label for="title" class="col-form-label">Remarks</label>
                            <input type="text" class="form-control" id="title" name="title" v-model="remarks" />
                        </div>
                        <div class="mb-2">
                            <label for="description" class="col-form-label">Duration:(HH:MM:SS)</label>
                            <input type="text" class="form-control" id="description" name="duration"
                                v-model="duration" />
                        </div>


                        <button type="submit" id="sbmt-btn" class="btn btn-outline-dark" @click="AddQuiz()">Add
                            Quiz</button>
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
                        <h1 class="modal-title fs-5" id="exampleModalLabel1">Edit Quiz</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="mb-2">
                            <label class="col-form-label">Remarks</label>
                            <input type="text" class="form-control" name="remarks" v-model="remarks">
                        </div>
                        <div class="mb-2">
                            <label class="col-form-label">Duration:(HH:MM:SS)</label>
                            <input type="text" class="form-control" name="duration" v-model="duration">
                        </div>


                        <button type="submit" class="btn btn-outline-dark" @click="editQuiz(this.quiz_id)">Save
                            Changes</button>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" hidden></button>

                    </div>
                    <div class="modal-footer"></div>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
import Sidebar from '@/components/sidebar.vue';
import Topbar from '@/components/Topbar.vue';


    export default {
        name: 'QuizList',
        components: {Sidebar, Topbar},
  
        props:["cid","cname","tquiz"],
        data() {
            return{
                quizes:[],
                remarks: null,
                duration:null,
                quiz_id:null,
            }
        },
        methods: {
            async fetchQuiz(){
                try {
                    const res = await fetch('http://localhost:5000/' + '/api/quizes/' + this.cid, {
                        headers: {
                            'Authentication-Token': JSON.parse(localStorage.getItem('user')).token
                        }
                    });
                    if (res.ok) {
                        this.quizes = await res.json();
                    }
                } catch (error) {
                    console.error(error)
                }
            },

            async AddQuiz(){
                try {
                    const res = await fetch('http://localhost:5000/' + 'api/quizes/' + this.cid, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'Authentication-Token': JSON.parse(localStorage.getItem('user')).token
                        },
                        body: JSON.stringify({ remarks: this.remarks, duration: this.duration })
                    })
                    if (res.ok) {
                        document.querySelector('#exampleModal .btn-close').click();
                        this.remarks = null;
                        this.duration = null;
                        await this.fetchQuiz();
                    } else {
                        const errorData = await res.json();
                        alert("Error: " + (errorData.message || "Invalid duration format!"));

                    }
                } catch (error) {
                    alert("Error: Could not connect to the server.");
                    console.log(error)
                }
            },
            async changeInit(quiz) {
                this.remarks = quiz.remarks;
                this.duration = quiz.duration;
                this.quiz_id = quiz.id;
            },
            async editQuiz(quiz_id) {
                try {
                    const res = await fetch('http://localhost:5000/' + 'api/quiz/' + quiz_id, {
                        method: 'PUT',
                        headers: {
                            'Content-Type': 'application/json',
                            'Authentication-Token': JSON.parse(localStorage.getItem('user')).token
                        },
                        body: JSON.stringify({ remarks: this.remarks, duration: this.duration.toString() })
                    })
                    if (res.ok) {
                        document.querySelector('#changeModal .btn-close').click();
                        this.remarks = null;
                        this.duration = null;
                        this.quiz_id = null;
                        await this.fetchQuiz();

                    } else {
                        const errorData = await res.json();
                        alert("Error: " + (errorData.message || "Invalid Input"));

                    }

                } catch (error) {
                    alert("Error: Could not connect to the server.");
                    console.log(error)
                }
            },
            async deleteQuiz(quiz_id) {
                try {
                    const res = await fetch('http://localhost:5000/' + '/api/quiz/' + quiz_id, {
                        method: 'DELETE',
                        headers: { 'Content-Type': 'application/json', 'Authentication-Token': JSON.parse(localStorage.getItem('user')).token }, body: JSON.stringify({ name: this.name, description: this.description })
                    })
                    if (res.ok) {
                        await this.fetchQuiz()

                    }
                } catch (err) {
                    console.error(err)
                }
            },
            getScore(scores) {
                const currentUser = JSON.parse(localStorage.getItem('user')).id;
                const scoreObj = scores.find(s => s.user_id === currentUser);
                return scoreObj ? scoreObj.total_score : 'Not Attempted'
            },

        },


        mounted(){
            this.fetchQuiz()
        }
    }
</script>

<style scoped>

</style>