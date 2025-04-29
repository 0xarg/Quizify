<template>
    <div>

        <div v-if="$store.state.loggedIn && $store.state.roles == 'admin'">
            <h1>This is Admin DashBoard</h1>

            <div class="dashboard-sections">
                <!-- View Subjects -->
                <div class="section">
                    <h2>📚 View Subjects</h2>
                    <p>Browse through available subjects.</p>
                    <button @click="$router.push({ name: 'SubjectList' })">View Subjects</button>
                </div>
            </div>
        </div>

        <!-- User Dash  -->
        <div v-if="$store.state.loggedIn && $store.state.roles == 'user'">
            <h1>Welcome to Dashoard</h1>
            <hr>
            <br>
            <button @click="create_csv" class='btn btn-warning'> Get Quiz Data </button>
            <hr>
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
    name: 'Admin-Dash',
    methods: {
        async create_csv() {
            console.log("Button clicked, create_csv method triggered");

            try{
                const res = await fetch('http://localhost:5000/'+ 'api/createCSV', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json', 'Authentication-Token': JSON.parse(localStorage.getItem('user')).token}
                })
                const task_id = (await res.json()).task_id;
                const interval = setInterval(async () => {
                    const res = await fetch(`http://localhost:5000/api/getCSV/${task_id}`, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'Authentication-Token': JSON.parse(localStorage.getItem('user')).token }
                    })
                    if (res.ok) {
                        console.log("Data is Ready");
                        window.open(`http://localhost:5000/api/getCSV/${task_id}`)
                        clearInterval(interval)
                    }
                },1000)
            }
            catch(error) {
                console.error("Error getting csv:", error)
                alert("Failed to Get CSV")
            }
        }
    }
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