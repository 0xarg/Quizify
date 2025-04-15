<template>
    <div>
        <hr>
        <h1
            @click="$router.push({name:'Chapter', params: {chapter_id: this.chapter_id}, query:{subject_id:this.subject_id}})">
            {{ name }}</h1>
        <h3>{{ subject_name }}</h3>
        <h3>{{ subject_id }}</h3>
        <h4>{{ description }}</h4>
        <p>Chapter Id: {{ chapter_id }}</p>
        <hr>
        <button v-if="$store.state.roles == 'admin'"
            @click="$router.push({ name: 'EditChapter', params: { chapter_id: this.chapter_id }})">Edit Chapter</button>
        <br>
        <button style="background-color: lightcoral;" @click='DeleteChapter'>delete</button>

    </div>
</template>

<script>
    export default {
        name: "ChapterCard",
        props: ["name","description","chapter_id","subject_id","subject_name"],
        methods: {
            async DeleteChapter() {
                const res = await fetch('http://localhost:5000/' + '/api/chapter/' + this.chapter_id, {
                    method: 'DELETE',
                    headers: { 'Content-Type': 'application/json', 'Authentication-Token': JSON.parse(localStorage.getItem('user')).token }
                })
                if (res.ok) {
                    alert("Chapter Deleted")
                    this.$router.push('/Chapters/'+this.subject_id).then(() => { window.location.reload() })






                }
            }

        },
    }
    


</script>

<style scoped>

</style>