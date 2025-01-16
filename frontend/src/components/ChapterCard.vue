<template>
    <div>
        <hr>
        <h1 @click="$router.push({name:'Chapter', params: {chapter_id: this.chapter_id}, query:{subject_id:this.subject_id}})"> {{ name }}</h1>
        <h3>{{ subject_name }}</h3>
        <h3>{{ subject_id }}</h3>
        <h4>{{ description }}</h4>
        <p>Chapter Id: {{ chapter_id }}</p>
        <hr>
    </div>
</template>

<script>
    export default {
        name: "ChapterCard",
        props: ["name","description","chapter_id","subject_id","subject_name"]
    }
    


</script>

<style scoped>

</style>