<template>
    <div>
        <router-link to='/'> Home </router-link>
        <router-link v-if="$store.state.loggedIn && $store.state.roles == 'admin'"  to='/dashboard'> Dash </router-link>
        <!-- <router-link v-if="$store.state.loggedIn && $state.store.roles == 'User'"  to='/'> U-Dash </router-link> -->
        <router-link to='/api/subjects'> View Subjects </router-link>
        <router-link to='/add-subjects'> Add Subject </router-link>
        <router-link to='/about'> About </router-link>
        <button v-if="$store.state.loggedIn" @click="$store.commit('logout')"> Logout </button>
        

        <router-link v-if="!$store.state.loggedIn" to='/login'> login </router-link>
    </div>

</template>


<script>

export default {
    name: 'Navbar'
}


</script>