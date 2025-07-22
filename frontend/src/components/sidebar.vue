<template>
    <div>
        <div class="sidebar">
            <div class="dash-logo"></div>
            <ul class="menu">
                <li class="active">
                    <a @click="$router.push({name:'dash'})">
                        <i class="fas fa-tachometer-alt"></i>
                        <span>Dashboard</span>
                    </a>
                </li>
                <li>
                    <a v-if="$store.state.roles == 'admin'" @click="$router.push({ name: 'AdminStats' })">
                        <i class="fas fa-square-poll-vertical"></i>
                        <span>Summary</span>
                    </a>
                    <a v-if="$store.state.roles == 'user'" @click="$router.push({ name: 'UserStats' })">
                        <i class="fas fa-square-poll-vertical"></i>
                        <span>Summary</span>
                    </a>
                </li>
                <li>
                    <a @click="$router.push({ name: 'SubjectList' })">
                        <i class="fas fa-chart-bar"></i>
                        <span>Subjects</span>
                    </a>
                </li>
                <!-- <li>
                    <a href="/camp_select">
                        <i class="fa-solid fa-snowflake"></i>
                        <span>Search Campaign</span>
                    </a>
                </li> -->
                <li>
                    <a href="#">
                        <i class="fas fa-cog"></i>
                        <span>Settings</span>
                    </a>
                </li>
                <li class="logout">
                    <a href="#" @click="logout">
                        <i class="fas fa-sign-out-alt"></i>
                        <span>Log Out</span>
                    </a>
                </li>

            </ul>

        </div>
    </div>
</template>

<script>
    export default {
        name:'Sidebar',
        methods:{
            logout(){
                this.$store.commit("logout");
                this.$router.push("/");
            }
        }
    }
</script>

<style scoped>
a{
    cursor: pointer;
}
</style>