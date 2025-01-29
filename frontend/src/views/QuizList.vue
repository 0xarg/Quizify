<template>
    <div>
        <h1> All Quiz of chapter: {{ chapter_id  }} 📑</h1>
        <!-- <ChapterCard v-for="chapter in chapters" :name = "chapter.name" :description = "chapter.description" :subject_id = "chpater.subject_id" :chapter_id = "chapter.id" :subject_name = "chapter['subject.name']"   /> -->
        <QuizCard v-for="quiz in quizes" :id = "quiz.id" :duration = "quiz.duration" :chapter_id="this.chapter_id" :chapter_name = "quiz['chapter.name']"  />
        
    </div>
</template>

<script>
import QuizCard from '@/components/QuizCard.vue';

    export default {
        name: 'QuizList',
        components: {
            QuizCard
        },
        props:["chapter_id"],
        data() {
            return{
                quizes:[]
            }
        },
        async mounted(){
            const res = await fetch('http://localhost:5000/' + '/api/quizes/' + this.chapter_id,{
                headers: {
                    'Authentication-Token': JSON.parse(localStorage.getItem('user')).token
                }
            })
            if (res.ok){
                this.quizes = await res.json()
            }else{
                alert('Quiz not Found')
                this.$router.push('/Subject/'+this.id)
            }
        }
    }
</script>

<style scoped>

</style>