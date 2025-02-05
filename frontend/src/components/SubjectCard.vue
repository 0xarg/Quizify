<template>
    <div>
        <!-- <h2 @click ="$router.push('/Subject/'+ subject_id)">{{ name }}</h2>
        <p>Description: {{ description }}</p>
        
        <p>Id: {{ subject_id }}</p>
        <hr> -->
        
        <!-- Button for Admin to Add Subject -->
        
        <!-- <h1>📚 All Subjects</h1> -->
        <div class="subject">
            <h2 @click="$router.push('/Subject/' + subject_id)" class="clickable">{{ name }}</h2>
            <p><strong>Description:</strong> {{ description }}</p>
            <p><strong>Subject ID:</strong> {{ subject_id }}</p>
            <hr>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'SubjectCard',
        props: ["name","description","subject_id"]
    }
</script>

<style scoped>

/* GPT Generated CSS */
.clickable {
    cursor: pointer;
    color: rgb(255, 72, 0);
    text-decoration: underline;
}

.clickable:hover {
    color: darkblue;
}

.subject {
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 8px;
    margin-bottom: 10px;
}

button {
    background-color: green;
    color: white;
    padding: 8px 15px;
    border: none;
    cursor: pointer;
    margin-bottom: 15px;
}
</style>