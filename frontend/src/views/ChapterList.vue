<template>
    <div class="dash-camp-body">
        <Sidebar/>

        <div class="main--content">
            <div class="header--wrapper">
                <div class="header--title">
                    <h2 v-if="chapters.length">{{ chapters[0]['subject.name'] }}</h2>
                    <span>Total Chapters: {{ chapters.length }}</span>
                </div>
                <div class="user--info">
                    <div class="search--box">
                        <i class="fa-solid fa-search"></i>
                        <input type="text" class="sin" name="" id="" placeholder="Search" />
                    </div>
                </div>
            </div>

            <div class="card--container">
                <h3 class="main--title">Chapters</h3>
                <div class="card--wrapper">
                    <div v-for="chapter in chapters" :key="chapter.id" class="camp--card">
                        <div class="card--header">
                            <div class="amount">
                                <span class="title">{{ chapter.name }}</span>
                                <span class="amount--value-camp"></span>
                                <span class="card--detail">{{ chapter.description }}</span>
                            </div>
                            <i class="fa-brands fa-canadian-maple-leaf"></i>
                        </div>
                        <div>
                            <button class="abtn" style="width: 100px" data-bs-toggle="modal"
                                data-bs-target="#changeModal" v-if="$store.state.roles == 'admin'"
                                @click="changeInit(chapter)">Change</button>
                        </div>
                        <div>
                            <button type="submit" @click="deleteChapter(chapter.id)" class="abtn" id="delbtn"
                                style="width: 100px; margin: 10px 0px" v-if="$store.state.roles == 'admin'">
                                Delete
                            </button>
                        </div>
                        <div>
                            <button class="abtn" style="text-decoration: none; color: chocolate;"
                                @click="$router.push({ name: 'QuizList', params: { chapter_id: chapter.id }, query: { chapter_name: chapter.name, totalQuiz: chapter.quizes.length } })">
                                View More
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
                        <h1 class="modal-title fs-5" id="exampleModalLabel">Add a Chapter</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="mb-2">
                            <label for="title" class="col-form-label">Name</label>
                            <input type="text" class="form-control" id="title" name="title" v-model="name" />
                        </div>
                        <div class="mb-2">
                            <label for="description" class="col-form-label">Description</label>
                            <input type="text" class="form-control" id="description" name="description"
                                v-model="description" />
                        </div>


                        <button type="submit" id="sbmt-btn" class="btn btn-outline-dark" @click="AddChapter()">Add
                            Chapter</button>
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
                        <h1 class="modal-title fs-5" id="exampleModalLabel1">Edit a Subject</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="mb-2">
                            <label class="col-form-label">Title</label>
                            <input type="text" class="form-control" name="title" v-model="name">
                        </div>
                        <div class="mb-2">
                            <label class="col-form-label">Description</label>
                            <input type="text" class="form-control" name="description" v-model="description">
                        </div>


                        <button type="submit" class="btn btn-outline-dark" @click="editChapter(this.chap_id)">Save
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
import Sidebar from '@/components/sidebar.vue'


    export default {
        name: 'ChapterList',
        components:{
            Sidebar
        },
    props: ["sid", "sname", "tchapters"],
        data() {
            return{
                chapters:[],
                name: null,
                description: null,
                chap_id: null,
            }
        },
        methods: {
            
            async fetchChapters(){
                try{
                    const res = await fetch('http://localhost:5000/' + '/api/chapters/' + this.sid, {
                        headers: {
                            'Authentication-Token': JSON.parse(localStorage.getItem('user')).token
                        }
                    })
                    if (res.ok) {
                        this.chapters = await res.json()
                    }
                }catch(err){
                    console.error(err)
                }
            },

            async AddChapter() {
                try {
                    const res = await fetch('http://localhost:5000/' + `/api/chapters/${this.sid}`, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json', 'Authentication-Token': JSON.parse(localStorage.getItem('user')).token }, body: JSON.stringify({ name: this.name, description: this.description })
                    })
                    if (res.ok) {
                        document.querySelector('#exampleModal .btn-close').click();
                        this.name = null;
                        this.description = null;
                        await this.fetchChapters();
                        // this.chapters = [...this.chapters];
                        // setTimeout(() => window.location.reload(),1000)  

                        
                    }

                } catch (err) {
                    console.error(err)
                }
            },
            async changeInit(chapter) {
                this.name = chapter.name;
                this.description = chapter.description;
                this.chap_id = chapter.id;
            },
            async editChapter(chapter_id) {
                try {
                    const res = await fetch('http://localhost:5000/' + 'api/chapter/' + chapter_id, {
                        method: 'PUT',
                        headers: { 'Content-Type': 'application/json', 'Authentication-Token': JSON.parse(localStorage.getItem('user')).token }, body: JSON.stringify({ name: this.name, description: this.description })
                    })
                    if (res.ok) {
                        document.querySelector('#changeModal .btn-close').click();
                        this.name = null;
                        this.description = null;
                        this.chap_id = null;
                        await this.fetchChapters();

                    } else {
                        const errorData = await res.json();
                        alert("Error: " + (errorData.message || "Invalid Input"));

                    }

                } catch (error) {
                    alert("Error: Could not connect to the server.");
                    console.log(error)
                }
            },
            async deleteChapter(chapter_id) {
                try {
                    const res = await fetch('http://localhost:5000/' + '/api/chapter/' + chapter_id, {
                        method: 'DELETE',
                        headers: { 'Content-Type': 'application/json', 'Authentication-Token': JSON.parse(localStorage.getItem('user')).token }, body: JSON.stringify({ name: this.name, description: this.description })
                    })
                    if (res.ok) {
                        await this.fetchChapters()
                    }
                } catch (err) {
                    console.error(err)
                }
            },
            

        },
       mounted(){
          this.fetchChapters()
        }
    }
</script>

<style scoped>

</style>