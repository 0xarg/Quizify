<template>
    <div>
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
                    console.log(this.selectedSubjs)
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

</style>