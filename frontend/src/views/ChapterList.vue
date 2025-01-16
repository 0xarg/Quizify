<template>
    <div>
        <h1> All Chapters 📑</h1>
        <!-- <ChapterCard v-for="chapter in chapters" :name = "chapter.name" :description = "chapter.description" :subject_id = "chpater.subject_id" :chapter_id = "chapter.id" :subject_name = "chapter['subject.name']"   /> -->
        <ChapterCard v-for="chapter in chapters" :name = "chapter.name" :description = "chapter.description" :subject_id = "chapter.subject_id" :chapter_id = "chapter.id" :subject_name = "chapter['subject.name']"  />
        
    </div>
</template>

<script>
import ChapterCard from '@/components/ChapterCard.vue';

    export default {
        name: 'ChapterList',
        components: {
            ChapterCard
        },
        props:["id"],
        data() {
            return{
                chapters:[]
            }
        },
        async mounted(){
            const res = await fetch('http://localhost:5000/' + '/api/chapters/' + this.id,{
                headers: {
                    'Authentication-Token': JSON.parse(localStorage.getItem('user')).token
                }
            })
            if (res.ok){
                this.chapters = await res.json()
            }else{
                alert('Chapter not Found')
                this.$router.push('/Subject/'+this.id)
            }
        }
    }
</script>

<style scoped>

</style>