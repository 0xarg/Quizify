<template>

    <body class="body-start-sponsor">
        <header>
            <h2 class="logo">Quizify</h2>
            <nav class="navigation">
                <a href="">Home</a>
                <a href="">About</a>
                <a href="">Services</a>
                <a href="">Contact</a>

            </nav>
        </header>
        <div class="wrapper">

            <div class="form-box Login">
                <h2>Login</h2>
                <!-- <button></button> -->
                <div class="input-box">
                    <span class="start-icon">
                        <ion-icon name="mail"></ion-icon>
                    </span>
                    <input type="email" required name="username" v-model="email">
                    <label for="Username">Email</label>

                </div>
                <div class="input-box">
                    <span class="start-icon"><ion-icon name="lock-closed"></ion-icon></span>
                    <input type="password" required name="password" v-model="password">
                    <label>Password</label>
                </div>
                <div class="remember-forget">
                    <label for=""><input type="checkbox">Remember me</label>
                    <a href="">Forget Password?</a>
                </div>
                <button @click='submitLogin' class="btn login-btn">Login</button>
                <div class="login-register">
                    <p>Don't have an account ? <a href="#" @click="$router.push({ name: 'registerUser' })">Register
                            now</a>
                    </p>
                </div>
            </div>
        </div>

    </body>
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
                try{
                    
                    const res = await fetch('http://localhost:5000' + '/login', {
                        method: 'POST',
                        headers:{'Content-Type':'application/json'}, body:JSON.stringify({email:this.email, password: this.password})})
                        if (res.ok){
                        const data = await res.json()
                        // Storing the token to authorize with each request
                        localStorage.setItem('user',JSON.stringify(data))
                        this.$store.commit('setUser')
                        this.$router.push('/dashboard')
                    } else {
                        alert("Please Enter valid Email/Password !!")
                        window.location.reload();
                    }
                }
                catch(err){
                    alert("Error: Could not connect to the Server.");
                    console.error(err)
                }
        }
        
    },

}
</script>

<style scoped>

</style>