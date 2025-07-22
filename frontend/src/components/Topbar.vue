<template>
    <div class="header--wrapper">
        <div class="header--title">
            <span >Welcome {{ uname }}</span>
            <span style="font-weight: bold; color:red "> {{ msg }}</span>
            <h2>{{ pname }}</h2>
            <span>{{ count }}</span>
            <!-- <h3>Ratings</h3> -->
        </div>
        <div class="user--info">
            <div class="search--box">

                <i class="fa-solid fa-search">

                </i>
                <input type="text" class="sin" name="" id="" placeholder="Search Subject">
            </div>
            <!-- <img src="/static/2.jpg" alt=""> -->

        </div>

    </div>
</template>

<script>
    export default {
        name:'Topbar',
      props:['pname','count','uname']
    }
</script>

<style scoped>

</style>