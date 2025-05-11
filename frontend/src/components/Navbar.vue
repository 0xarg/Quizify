<template>
    <div>


        <div v-if="isLoggedIn && isAdmin">
            <!-- Admin Based Links -->
            <router-link to='/' class="router-link-padding"> Home </router-link>
            <router-link to='/dashboard' class="router-link-padding"> Dash </router-link>
            <router-link to='/subjects' class="router-link-padding"> View Subjects </router-link>
            <router-link to='/add-subjects' class="router-link-padding"> Add Subject </router-link>
            <router-link to='/about' class="router-link-padding"> About </router-link>
            <router-link to='/AllSubjects' class="router-link-padding"> All Subjects </router-link>
            <button v-if="$store.state.loggedIn" @click="logout"> Logout </button>
            <router-link v-if="!$store.state.loggedIn" to='/'> login </router-link>
        </div>


        <!-- User Based Links -->
        <div v-if="isLoggedIn && isUser">
            
            <router-link to='/dashboard' class="router-link-padding"> Dash </router-link>


        </div>


    </div>



</template>


<script>

export default {
    name: 'Navbar',
    computed: {
        isLoggedIn() {
            console.log('isLoggedIn:', this.$store.state.loggedIn);
            return this.$store.state.loggedIn;
        },
        isAdmin() {
            console.log('isAdmin:', this.$store.state.roles == 'admin');
            return this.$store.state.roles == 'admin';
        },
        isUser() {
            console.log('user:', this.$store.state.roles == 'user');
            return this.$store.state.roles == 'user';
        }
    },
    methods: {
        logout(){
            this.$store.commit('logout');
            this.$router.push('/')
        }
    }
}


</script>

<style>
.router-link-padding {
    padding: 10px;
    margin-right: 10px;
    /* Optional: Adds space between the links */
    text-decoration: none;
    /* Optional: removes underline from links */
}
</style>