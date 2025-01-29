<template>
    <div>
        <h1>{{ quiz.id }}</h1>
        <h3>{{ quiz.duration }}</h3>
        <h4> {{ quiz.date }}</h4>
        <h4>{{ quiz.remarks }}</h4>

    </div>
</template>

<script>
    export default {
        name: "QuizDisplay",
        props:["quiz_id","cid"],
        data(){
            return{
                quiz:[]
            }
        },
        async mounted(){
            const res = await fetch('http://localhost:5000/' + '/api/quiz/' + this.quiz_id,{
                headers: {
                    'Authentication-Token': JSON.parse(localStorage.getItem('user')).token
                }
            })
            if (res.ok){
                this.quiz = await res.json()
            }else{
                alert('Chapter not Found')
                this.$router.push('/api/chapters/'+subject_id)
            }

        }

    }
</script>

<style scoped>

</style>