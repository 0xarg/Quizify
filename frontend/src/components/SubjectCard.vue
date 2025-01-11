<template>
    <div>
        <h2> {{ name }}</h2>
        <hr>
        <p>{{ description }}</p>

        <p>{{ subject_id }}</p>
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