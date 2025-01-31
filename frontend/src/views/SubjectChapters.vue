<template>
    <div>
        <h1>All Subjects and their Chapters 📚</h1>
        <div v-for="subject in subjects">
            <h3 @click ="$router.push('/Subject/'+ subject.id)" style="cursor:pointer;">{{ subject.name }}</h3>
            <ol >
                <li v-for="chapter in subject.chapters" 
                 @click="$router.push({name:'Chapter', params: {chapter_id: chapter.id}, query:{sid: chapter.subject_id}})"
                  style="cursor:pointer;">
                 <strong>{{ chapter.name }}</strong>
                </li>
            </ol>
            <hr>
    
        </div>
    </div>
</template>



<script>
export default {
        name:'SubjectChapters',
        
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