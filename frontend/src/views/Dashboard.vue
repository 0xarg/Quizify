<template>
    <div class="dash-body">

        <Sidebar />
        <div class="main--content">
            <Topbar :uname="$store.state.username" @search-subject="handleGlobalSearch" />

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
                            <i class="fas  fa-building-columns dash-icon dark-purple"></i>

                        </div>

                    </div>
                    <div class="payment--card light-green" v-if="$store.state.roles == 'admin'">
                        <div class="card--header">
                            <div class="amount">
                                <span class="title">
                                    Total Users
                                </span>
                                <br>
                                <span class="amount--value">
                                    {{ users.length }}
                                </span>

                            </div>
                            <i class="fas dash-icon f fa-users dark-blue"></i>
                        </div>

                    </div>




                    <div v-if="$store.state.roles == 'user'" class="payment--card light-green">
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
            <div class="card--container" v-if="$store.state.roles == 'admin'">
                <div class="chck-boxes">
                    <label for="filter_User">Show Users Only</label>
                    <input type="checkbox" v-model="isChecked" name="filter_User" id="">
                </div>

            </div>
            <div v-if="!isChecked">

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
                                    <td>{{ subject.name }}</td>
                                    <td>{{ subject.description }}</td>
                                    <td> {{ subject.chapters ? subject.chapters.length : 0 }}</td>
                                    <td><button class="yellow-btn"
                                            @click="$router.push({ name: 'ChapterList', params: { subject_id: subject.id } })">View</button>
                                    </td>


                                </tr>
                            </tbody>

                        </table>
                    </div>
                </div>
            </div>

            <div v-if="!isChecked">


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
                                    <td>{{ chapter.subjectName }}</td>
                                    <td> {{ chapter.description }} </td>
                                    <td><button class="yellow-btn"
                                            @click="$router.push({ name: 'QuizList', params: { chapter_id: chapter.id } })">View</button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
            <div v-if="!isChecked">
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
                                    <td>Quiz {{ quiz.id }}</td>
                                    <td>{{ quiz.chapterName }}</td>
                                    <td> {{ quiz.duration }}</td>
                                    <td v-if="$store.state.roles == 'admin'"><button
                                            @click="$router.push({ name: 'Quiz', params: { quiz_id: quiz.id } })"
                                            class="green-btn">View</button></td>
                                    <td v-if="$store.state.roles == 'user'"><button
                                            @click="$router.push({ name: 'QuizTake', params: { quiz_id: quiz.id }, query: {cid: quiz.chapter_id} })"
                                            class="green-btn">Take Quiz</button>
                                    </td>
                                </tr>
                            </tbody>

                        </table>
                    </div>
                </div>
            </div>

            <div class="tabular--wrapper" v-if="$store.state.roles == 'admin'">
                <h3 class="main--title"> Users</h3>
                <div class="table--container">
                    <table>
                        <thead>
                            <tr>
                                <th>Name</th>
                                <th>Email</th>
                                <th>Take Action</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="user in users" :key="user.id">
                                <td>{{ user.email.split('@')[0] }}</td>
                                <td>{{ user.email }}</td>
                                <td> <button class="red-btn" @click="deleteUser(user.id)">Delete</button></td>
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
import axios from 'axios';

import Topbar from '@/components/Topbar.vue';

export default {
    name: 'Admin-Dash',
    components: {
        Sidebar, Topbar
    },
    data() {
        return {
            subjects: [],
            users: [],
            isChecked: false,
        }
    },
    methods: {
        logout() {
            localStorage.removeItem('user')
            this.$router.push('/')
        },


        async searched_subjs(searchTerm) {
            axios.get(`http://localhost:5000/api/subjects?search=${searchTerm}`)
                .then(res => {
                    this.subjects = res.data;
                });
        },
        async searched_users(searchTerm) {
            try {
                axios.get(`http://localhost:5000/api/users?search=${searchTerm}`,{
                    headers:{
                        'Authentication-Token': JSON.parse(localStorage.getItem('user')).token
                    }
                })
                    .then(res => {
                        this.users = res.data;
                    });
            } catch (error) {
                console.error(error);
                                
            }
        },
        async handleGlobalSearch(searchTerm) {
            if (this.isChecked) {
                this.searched_users(searchTerm);
            } else {
                this.searched_subjs(searchTerm);
                this.searched_users(searchTerm);
            }
        },

        async getAllUsers(){

            try {
                await axios.get("http://localhost:5000/api/users",{
                    headers:{
                        'Authentication-Token': JSON.parse(localStorage.getItem('user')).token
                    }
                }).then(res=>{
                    this.users = res.data
                })
            } catch (error) {
                console.error("Error fetching users", error)
            }


        },

        async deleteUser(user_id){
            try {
                await axios.delete(`http://localhost:5000/api/users/${user_id}`,{
                    headers:{
                        'Authentication-Token': JSON.parse(localStorage.getItem('user')).token
                    }
                });
                await this.getAllUsers()  
            } catch (error) {
                console.error(error);
            }
        },


        async create_csv() {

            try {
                const res = await fetch('http://localhost:5000/' + 'api/createCSV', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json', 'Authentication-Token': JSON.parse(localStorage.getItem('user')).token }
                })
                const task_id = (await res.json()).task_id;
                const interval = setInterval(async () => {
                    const res = await fetch(`http://localhost:5000/api/getCSV/${task_id}`, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'Authentication-Token': JSON.parse(localStorage.getItem('user')).token
                        }
                    })
                    if (res.ok) {
                        console.log("Data is Ready");
                        window.open(`http://localhost:5000/api/getCSV/${task_id}`)
                        clearInterval(interval)
                    } else {
                        alert("Error connecting Backend");
                        clearInterval(interval)
                    }
                }, 1000)
            }
            catch (error) {
                console.error("Error getting csv:", error)
                alert("Failed to Get CSV")
            }
        },
        async fetch_data() {
            try {
                const res = await fetch('http://localhost:5000' + '/api/subjects', {
                    method: 'GET',
                    headers: { 'Content-Type': 'application/json', 'Authentication-Token': JSON.parse(localStorage.getItem('user')).token }
                });
                if (res.ok) {
                    const data = await res.json();
                    this.subjects = data;
                    console.log("ok")
                }
            } catch (err) {
                console.error("Failed to fetch Data", err)
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
            this.subjects.forEach(subject => {
                (subject.chapters || []).forEach(chapter => {
                    (chapter.quizes || []).forEach(quiz => {
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
        this.getAllUsers()
    }
}
</script>

<style scoped></style>