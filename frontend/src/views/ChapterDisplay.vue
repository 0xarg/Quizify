<template>
    <div>
        <h1>{{ chapter.name }}</h1>
        <h3>{{ chapter.description }}</h3>
        <h4> Chapter_id: {{ chapter_id }}</h4>
        <h4>SUbject_id: {{ subject_id }}</h4>
    </div>
</template>

<script>
    export default {
        name: "ChapterDisplay",
        props:["subject_id","chapter_id"],
        data(){
            return{
                chapter:[]
            }
        },
        async mounted(){
            const res = await fetch('http://localhost:5000/' + '/api/chapter/' + this.chapter_id,{
                headers: {
                    'Authentication-Token': JSON.parse(localStorage.getItem('user')).token
                }
            })
            if (res.ok){
                this.chapter = await res.json()
            }else{
                alert('Chapter not Found')
                this.$router.push('/api/chapters/'+subject_id)
            }

        }

    }
</script>

<style scoped>

</style>