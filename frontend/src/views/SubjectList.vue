<template>
    <div>
        <h1>All Subjects 📚</h1>
        <SubjectCard v-for="subject in subjects" :name = "subject.name" :description = "subject.description" :subject_id = "subject.id"/>
    </div>
</template>



<script>
import SubjectCard from '@/components/SubjectCard.vue'
export default {
        name:'SubjectList',
        components: {
            SubjectCard
        },
        data(){
            return{
                subjects:[]
            }
        },

        async mounted(){
            const res = await fetch('http://localhost:5000/' + '/api/subjects',{
                headers: {
                    'Authentication-Token': JSON.parse(localStorage.getItem('user')).token
                }
            })
            this.subjects = await res.json()

        }
    }
</script>

<style scoped>

</style>