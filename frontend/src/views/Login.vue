<template>
    <div>
        <h3>Login Form</h3>
        <input placeholder="email" v-model = "email"/>
        <input placeholder="password" v-model = "password"/>
        <button @click='submitLogin'>Login</button>
    </div>
</template>

<script>
    export default {
        name:'Login',
        data() {
            return{
                email: null,
                password: null,
            }
        },
        methods: {
            async submitLogin(){
                const res = await fetch('http://localhost:5000/' + '/login', {
                    method: 'POST',
                    headers:{'Content-Type':'application/json'}, body:JSON.stringify({email:this.email, password: this.password})})
                    if (res.ok){
                console.log('We are Logged in')
                const data = await res.json()
                console.log(data)
                    
                    
                    
            }
        }
        
    },
    mounted() {
  console.log('Login component mounted');
},
}
</script>

<style scoped>

</style>