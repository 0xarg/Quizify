<template>
    <div>

        <div v-if="$store.state.loggedIn && $store.state.roles == 'admin'">
            <h1>This is Admin DashBoard</h1>
        </div>

        <!-- User Dash  -->
        <div v-if="$store.state.loggedIn && $store.state.roles == 'user'">
            <h1>Welcome to  Dashoard</h1>

            <div class="dashboard-sections">
                <!-- View Subjects -->
                <div class="section">
                    <h2>📚 View Subjects</h2>
                    <p>Browse through available subjects.</p>
                    <button @click="$router.push({ name: 'SubjectList' })">View Subjects</button>
                </div>

                <!-- Take a Quiz -->
                <div class="section">
                    <h2>📝 Take a Quiz</h2>
                    <p>Start a quiz and test your knowledge.</p>
                    <button @click="$router.push({ name: 'TakeQuiz' })">Take a Quiz</button>
                </div>

                <!-- View Quiz History -->
                <div class="section">
                    <h2>📜 View Quiz History</h2>
                    <p>Check your past quiz attempts.</p>
                    <button @click="$router.push({ name: 'QuizHistory' })">View History</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Admin-Dash'
}
</script>

<style  scoped>

h1 {
    background-color: antiquewhite;
}

.dashboard-sections {
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.section {
    border: 1px solid #ccc;
    padding: 15px;
    border-radius: 10px;
}

button {
    background-color: blue;
    color: white;
    padding: 8px 15px;
    border: none;
    cursor: pointer;
    margin-top: 10px;
}

</style>