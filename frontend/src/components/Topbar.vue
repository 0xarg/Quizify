<template>
    <div class="header--wrapper">
        <div class="header--title">
            <span style="font-size: 15px;">Welcome <span style="font-size: 20px; color: darkred; font-weight: 800;">{{
                    uname }} </span> </span>
            <h2>{{ pname }}</h2>
            <span>{{ count }}</span>
            <!-- <h3>Ratings</h3> -->
        </div>
        <div>
            <span>{{ currentTime }}</span>
        </div>
        <div class="user--info">

            <div class="search--box">

                <i class="fa-solid fa-search">

                </i>
                <input type="text" class="sin" placeholder="Search" v-model="search" @input="handleSearch" />

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
      },
      computed:{
          currentTime() {
              return new Date().toLocaleDateString('en-US', {
                  weekday: 'long',
                  day: '2-digit',
                  month: 'long',
                //   year: 'numeric'
              });
          }
      }
    }
</script>

<style scoped>

</style>