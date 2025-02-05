<template>
    <div>


        <div v-if="$store.state.loggedIn && $store.state.roles == 'admin'">
            <!-- Admin Based Links -->
            <router-link to='/' class="router-link-padding"> Home </router-link>
            <router-link to='/dashboard' class="router-link-padding"> Dash </router-link>
            <router-link to='/api/subjects' class="router-link-padding"> View Subjects </router-link>
            <router-link to='/add-subjects' class="router-link-padding"> Add Subject </router-link>
            <router-link to='/about' class="router-link-padding"> About </router-link>
            <router-link to='/AllSubjects' class="router-link-padding"> All Subjects </router-link>
            <button v-if="$store.state.loggedIn" @click="$store.commit('logout')"> Logout </button>
            <router-link v-if="!$store.state.loggedIn" to='/login'> login </router-link>
        </div>


        <!-- User Based Links -->
        <div v-if="$store.state.loggedIn && $store.state.roles == 'user'">
            
            <router-link to='/dashboard' class="router-link-padding"> Dash </router-link>


        </div>


    </div>



</template>


<script>

export default {
    name: 'Navbar'
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