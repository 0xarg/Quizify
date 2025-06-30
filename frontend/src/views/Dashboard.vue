<template>
    <div class="dash-body">

        <Sidebar />
        <div class="main--content">
            <div class="header--wrapper">
                <div class="header--title">
                    <span>Welcome </span> <span style="font-weight: bold; text-decoration:underline ">{{ uname }}</span>
                    <br>
                    <span style="font-weight: bold; color:red "> {{ msg }}</span>
                    <h2>Dashboard</h2>
                    <!-- <h3>Ratings</h3> -->
                </div>
                <div class="user--info">
                    <div class="search--box">

                        <i class="fa-solid fa-search">

                        </i>
                        <input type="text" class="sin" name="" id="" placeholder="Search Subject">
                    </div>
                    <!-- <img src="/static/2.jpg" alt=""> -->

                </div>

            </div>

            <div class="card--container">
                <h3 class="main--title">
                    Today's data
                </h3>
                <div class="card--wrapper">
                    <div class="payment--card light-red">
                        <div class="card--header">
                            <div class="amount">
                                <span class="title">
                                    Total Subjects
                                </span>
                                <br>
                                <span class="amount--value">
                                    {{ subjects.length }}
                                </span>

                            </div>
                            <i class="fas dash-icon fa-duotone fa-thin fa-book dark-green"></i>
                        </div>

                    </div>

                    <div class="payment--card light-blue">
                        <div class="card--header">
                            <div class="amount">
                                <span class="title">
                                    Total Chapters
                                </span>
                                <br>
                                <span class="amount--value">
                                    {{subjects.reduce((sum, s) => sum + (s.chapters ? s.chapters.length : 0), 0)}}
                                </span>

                            </div>
                            <i class="fas dash-icon fa-thin fa-bookmark"></i>
                        </div>

                    </div>



                    <div class="payment--card light-purple">
                        <div class="card--header">
                            <div class="amount">
                                <span class="title">
                                    Total Quizes
                                </span>
                                <br>
                                <span class="amount--value">
                                    {{subjects.reduce((sum, s) => sum + (s.chapters ? s.chapters.reduce((cSum, c) =>
                                    cSum + (c.quizes ? c.quizes.length : 0), 0) : 0), 0)}}
                                </span>

                            </div>
                            <i class="fas dash-icon fa-thin fa-building-columns dark-purple"></i>

                        </div>

                    </div>




                    <div  v-if="$store.state.roles == 'user'" class="payment--card light-green">
                        <div class="card--header">
                            <div class="amount">
                                <span class="title">
                                    <a @click="create_csv" style="cursor: pointer;">Create CSV</a>
                                </span>
                                <br>
                                <span class="amount--value">
                                </span>

                            </div>
                            <i class="fas fa-check dash-icon dark-blue"></i>
                        </div>

                    </div>

                </div>
            </div>
            <div class="tabular--wrapper">
                <h3 class="main--title"> Subjects</h3>
                <div class="table--container">
                    <table>
                        <thead>
                            <tr>
                                <th>Name </th>
                                <th>Description</th>
                                <th>Total Chapters</th>
                                <th>Action</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="subject in subjects" :key="subject.id">
                                <td>{{subject.name}}</td>
                                <td>{{subject.description}}</td>
                                <td> {{subject.chapters ? subject.chapters.length : 0}}</td>
                                <td><button class="yellow-btn" @click="$router.push({name:'ChapterList',params:{subject_id:subject.id}})">View</button></td>


                            </tr>
                        </tbody>

                    </table>
                </div>
            </div>
            <div class="tabular--wrapper">
                <h3 class="main--title"> Chapters</h3>
                <div class="table--container">
                    <table>
                        <thead>
                            <tr>
                                <th>Name </th>
                                <th>Subject</th>
                                <th>Description</th>
                                <th>Action</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="chapter in allChapters" :key="chapter.id">
                                <td>{{ chapter.name }}</td>
                                <td>{{chapter.subjectName}}</td>
                                <td> {{chapter.description}} </td>
                                <td><button class="yellow-btn" @click="$router.push({name:'QuizList', params:{chapter_id:chapter.id}})">View</button></td>
                            </tr>
                        </tbody>
                    </table>
                </div>

            </div>
            <div class="tabular--wrapper">
                <h3 class="main--title"> Quizes</h3>
                <div class="table--container">
                    <table>
                        <thead>
                            <tr>
                                <th>Name</th>
                                <th>Chapter</th>
                                <th>Duration</th>
                                <th>View Quiz</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="quiz in allQuizzes" :key="quiz.id">
                                <td>Quiz {{quiz.id}}</td>
                                <td>{{quiz.chapterName}}</td>
                                <td> {{quiz.duration}}</td>
                                <td v-if="$store.state.roles == 'admin'"><button @click="$router.push({name:'Quiz', params:{quiz_id:quiz.id}})" class="green-btn">View</button></td>
                                <td v-if="$store.state.roles == 'user'"><button class="green-btn">Take Quiz</button></td>
                            </tr>
                        </tbody>

                    </table>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
import Sidebar from '@/components/sidebar.vue';

export default {
    name: 'Admin-Dash',
    components:{
        Sidebar
    },
    data(){
        return{
            subjects: [],
        }
    },
    methods: {
        logout(){
            localStorage.removeItem('user')
            this.$router.push('/')
        },


        async create_csv() {
            console.log("Button clicked, create_csv method triggered");

            try{
                const res = await fetch('http://localhost:5000/'+ 'api/createCSV', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json', 'Authentication-Token': JSON.parse(localStorage.getItem('user')).token}
                })
                const task_id = (await res.json()).task_id;
                const interval = setInterval(async () => {
                    const res = await fetch(`http://localhost:5000/api/getCSV/${task_id}`, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'Authentication-Token': JSON.parse(localStorage.getItem('user')).token }
                    })
                    if (res.ok) {
                        console.log("Data is Ready");
                        window.open(`http://localhost:5000/api/getCSV/${task_id}`)
                        clearInterval(interval)
                    }else{
                        alert("Error connecting Backend");
                        clearInterval(interval)
                    }
                },1000)
            }
            catch(error) {
                console.error("Error getting csv:", error)
                alert("Failed to Get CSV")
            }
        },
        async fetch_data(){
            try{
                const res = await fetch('http://localhost:5000'+'/api/subjects', {
                    method: 'GET',
                    headers: { 'Content-Type': 'application/json', 'Authentication-Token': JSON.parse(localStorage.getItem('user')).token }
                });
                if (res.ok) {
                    const data = await res.json();
                    this.subjects = data;
                    console.log("ok")
                }
            }catch (err){
                console.error("Failed to fetch Data",err)
            }
        }
    },
    computed: {
        allChapters() {
            let chapters = [];
            this.subjects.forEach(subject => {
                (subject.chapters || []).forEach(chapter => {
                    chapters.push({
                        ...chapter,
                        subjectName: subject.name
                    });
                });
            });
            return chapters;
        },
        allQuizzes() {
            let quizzes = [];
            this.subjects.forEach(subject=>{
                (subject.chapters || []).forEach(chapter =>{
                    (chapter.quizes || []).forEach(quiz=>{
                        quizzes.push({
                            ...quiz,
                            chapterName: chapter.name
                        });
                    });
                });
            });
            return quizzes
        }
    },
    mounted() {
        this.fetch_data();
    }
}
</script>

<style  scoped>

</style>