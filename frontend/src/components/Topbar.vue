<template>
    <div class="header--wrapper">
        <div class="header--title">
            <span>Welcome {{ uname }}</span>
            <h2>{{ pname }}</h2>
            <span>{{ count }}</span>
            <!-- <h3>Ratings</h3> -->
        </div>
        <div class="user--info">
            <div class="search--box">

                <i class="fa-solid fa-search">

                </i>
                <input type="text" class="sin" placeholder="Search Subject" v-model="search" @input="handleSearch" />

            </div>

        </div>

    </div>
</template>

<script>
    export default {
        name:'Topbar',
      props:['pname','count','uname'],
      data (){
        return{
            search:''
        }
      },
      methods:{
        handleSearch(){
            this.$emit('search-subject', this.search)
        }
      }
    }
</script>

<style scoped>

</style>