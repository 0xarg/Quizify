<template>
    <div>
        <span>Name of the Subject: <h2 style="display: inline;">{{ name }}</h2></span>
        <p>Description: {{ description }}</p>
        
        <p>Id: {{ subject_id }}</p>
        <hr>
    </div>
</template>

<script>
    export default {
        name: 'SubjectCard',
        props: ["name","description","subject_id"]
    }
    console.log('SC added')
</script>

<style scoped>

</style>