<template>
    <div class="dash-camp-body">
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

        <div class="main--content">
            <div class="header--wrapper">
                <div class="header--title">
                    <span>Welcome {{ uname }}</span>
                    <h2>Dashboard</h2>
                </div>
                <div class="user--info">
                    <div class="search--box">
                        <i class="fa-solid fa-search"></i>
                        <input type="text" class="sin" name="" id="" placeholder="Search" />
                    </div>
                </div>
            </div>

            <div class="card--container">
                <h3 class="main--title">Subjects</h3>
                <div class="card--wrapper">
                    <div v-for="subject in subjects" :key="subject.id" class="camp--card">
                        <div class="card--header">
                            <div class="amount">
                                <span class="title">Title</span>
                                <span class="amount--value-camp">{{ subject.name }}</span>
                                <span class="card--detail">{{ subject.description }}</span>
                            </div>
                            <i class="fa-brands fa-canadian-maple-leaf"></i>
                        </div>
                        <div>
                            <button class="abtn" style="width: 100px" data-bs-toggle="modal"
                                data-bs-target="#changeModal" v-if="$store.state.roles == 'admin'"
                                @click="changeInit(subject)">Change</button>
                        </div>
                        <div>
                            <button type="submit" @click="deleteSub(subject.id)" class="abtn" id="delbtn"
                                style="width: 100px; margin: 10px 0px" v-if="$store.state.roles == 'admin'">
                                Delete
                            </button>
                        </div>
                        <div>
                            <button class="abtn" style="text-decoration: none; color: chocolate;">
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
                        <h1 class="modal-title fs-5" id="exampleModalLabel">Add a Subject</h1>
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


                        <button type="submit" id="sbmt-btn" class="btn btn-outline-dark" @click="AddSubject">Add
                            Subject</button>
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


                            <button type="submit" class="btn btn-outline-dark" @click="editSubject(this.sub_id)">Save Changes</button>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" hidden></button>

                    </div>
                    <div class="modal-footer"></div>
                </div>
            </div>
        </div>

    </div>
</template>



<script>
export default {
        name:'SubjectList',

        data(){
            return{
                name: null,
                description: null,
                sub_id: null,
                subjects:[]
            }
        },
    methods: {
        async fetchSubjects() {
            try {
                const res = await fetch('http://localhost:5000/' + '/api/subjects', {
                    headers: {
                        'Authentication-Token': JSON.parse(localStorage.getItem('user')).token
                    }
                })
                if (res.ok) {
                    this.subjects = await res.json()
                }
            } catch (err) {
                console.error(err);
            }

        },
        async AddSubject() {
            try{
                const res = await fetch('http://localhost:5000/' + '/api/subjects', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json', 'Authentication-Token': JSON.parse(localStorage.getItem('user')).token }, body: JSON.stringify({ name: this.name, description: this.description })
                })
                if (res.ok) {
                    document.querySelector('#exampleModal .btn-close').click();
                    this.name = null;
                    this.description = null;

                    await this.fetchSubjects();
                }

            }catch (err){
                console.error(err)
            }
        },

        async deleteSub(subject_id) {
            try{
                const res = await fetch('http://localhost:5000/' + '/api/subjects/' + subject_id, {
                    method: 'DELETE',
                    headers: { 'Content-Type': 'application/json', 'Authentication-Token': JSON.parse(localStorage.getItem('user')).token }, body: JSON.stringify({ name: this.name, description: this.description })
                })
                if (res.ok) {
                    this.$router.push('/subjects').then(() => { window.location.reload() })

                }
            }catch (err){
                console.error(err)
            }
        },
        
        async changeInit(subject){
            this.name = subject.name;
            this.description = subject.description;
            this.sub_id = subject.id;
        },
        
        async editSubject(subject_id){
            try {
                const res = await fetch('http://localhost:5000/' + 'api/subjects/' + subject_id, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json', 'Authentication-Token': JSON.parse(localStorage.getItem('user')).token }, body: JSON.stringify({ name: this.name, description: this.description })
                })
                console.log(this.description)
                if (res.ok) {
                    document.querySelector('#changeModal .btn-close').click();
                    this.name = null;
                    this.description = null;
                    this.sub_id = null;

                    await this.fetchSubjects();
                } else {
                    const errorData = await res.json();
                    alert("Error: " + (errorData.message || "Invalid Input"));
                    
                }

            } catch (error) {
                alert("Error: Could not connect to the server.");
                console.log(error)
            }
        },
        
        
    },
    mounted() {
        this.fetchSubjects();
    }

    }
</script>

<style scoped>

</style>