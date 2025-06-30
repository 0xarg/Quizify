<template>
    <!-- <div>
        <h3>Register</h3>
        <label for="email">Email</label>
        <input name="email" placeholder="Email" v-model = "email">
        <br>
        <label for="password">Email</label>
        <input name="password" placeholder="Password" type="password" v-model = "password">
        <br>
        <label for="subjects">Prefered Subjects</label>
        <select name="subjects" multiple SE v-model="selectedSubjs">
            <option v-for="subject in subjects" :key="subject.id" :value="subject.name">{{ subject.name }}</option>
        </select>
        <br>
        <button @click="registerUser"> Register</button>
    </div> -->
    <div>
        <div class="body-start">
            <!--------------------------------Navbar----Start------------------------------------------------------------------------------------------------>
            <header>
                <h2 class="logo">InfluenSync</h2>
                <nav class="navigation">
                    <a href="">Home</a>
                    <a href="">About</a>
                    <a href="">Services</a>
                    <a href="">Contact</a>


                </nav>
            </header>
            <!--------------------------------Navbar----End------------------------------------------------------------------------------------------------>





            <!--------------------------------Login----Start------------------------------------------------------------------------------------------------>
            <div class="rwrapper">
                <form @submit.prevent="registerUser">
                    <h1>User Registration</h1>

                    <div class="rinput-box">
                        <div class="rinput-field">
                            <input type="text" placeholder="Email" name="email" v-model="email">
                            <i><ion-icon name="person"></ion-icon></i>
                        </div>
                        <div class="rinput-field">
                            <input type="password" placeholder="Password" v-model="password" name="password">
                            <i><ion-icon name="logo-web-component"></ion-icon></i>
                        </div>
                    </div>


                    <div class="rinput-box">
                        <div class="rinput-field">
                            <select multiple v-model="selectedSubjs">
                                <option v-for="subject in subjects" :key="subject.id" :value="subject.name">{{
                                    subject.name }}</option>
                            </select>
                            <i><ion-icon name="albums"></ion-icon></i>
                        </div>

                    </div>



                    <label for="" class="rlabel"><input type="checkbox" class="rinput"> I herby declare that the above
                        information provided is true and correct</label>

                    <button class="rbtn">Register</button>
                    <div class="login-register">
                        <p>Already have an account ? <a href="#" @click="$router.push({name:'Login'})">Login now</a></p>

                    </div>
                </form>

            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "RegisterUser",
        data() {
            return {
                email: "",
                password: "",
                subjects: [],
                selectedSubjs: []
            };
        },
        methods: {
            async getSubjects(){
                try{
                    const res = await fetch('http://localhost:5000/' + 'api/subjects', {
                
                    })
                    this.subjects = await res.json()
                } catch(error) {
                    console.log("Error getting subjects",error)
                }
            },

            async registerUser(){
                try {
                    const res = await fetch('http://localhost:5000/' + '/api/users', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({email : this.email, password : this.password, pref_subjects : this.selectedSubjs})
                    })
                    alert("User Registered Successfully")
                    this.$router.push('/')

                } catch(error) {
                    console.error("Error adding User:",error)
                    alert("Failed to register User")

                }

            }
        },
        mounted() {
            this.getSubjects();
        }

    }
</script>

<style scoped>
/* Reset .rinput-field to be positioned relative */
.rinput-field {
    position: relative;
}

/* Style the select to look like an input */
.rinput-field select {
    width: 100%;
    padding: 12px 16px 12px 42px;
    /* extra left padding for icon */
    border: 2px solid #888;
    border-radius: 5px;
    font-size: 1rem;
    font-family: inherit;
    /* box-sizing: border-box; */
    background-color: white;
}

/* Make multi-select height consistent */
.rinput-field select[multiple] {
    height: 48px;
    overflow-y: auto;
}

/* Position the icon absolutely */
.rinput-field i {
    position: absolute;
    top: 50%;
    left: 12px;
    transform: translateY(-50%);
    pointer-events: none;
    font-size: 1.2rem;
    color: #555;
}
</style>