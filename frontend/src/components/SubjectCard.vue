<template>
    <div>
        <h2 @click ="$router.push('/Subject/'+ subject_id)">{{ name }}</h2>
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
</script>

<style scoped>

</style>