<template>
    <div>
        <h3>Edit Quiz</h3>
        <p>For Quiz no.{{ quiz_id }}</p>
        <label for="remarks">Remarks: </label>
        <input  id="remarks" placeholder="remarks" v-model="remarks" />
        <br>
        <br>
        <label for="duration">Duration:(HH:MM:SS) </label>
        <input id="duration" placeholder="HH:MM:SS" v-model="duration" />
        <br>
        <br>
        <button @click='EditQuiz'>Edit Quiz</button><br>

    </div>
</template>

<script>
export default {
    name: 'EditQuiz',
    props: ["quiz_id","cid"],
    data() {
        return {
            duration: null,
            remarks: null,
        }
    },
    methods: {
        async EditQuiz() {
            try {
                const res = await fetch('http://localhost:5000/' + 'api/quiz/' + this.quiz_id, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authentication-Token': JSON.parse(localStorage.getItem('user')).token},
                    body: JSON.stringify({ remarks: this.remarks, duration: this.duration.toString() })
                })
                if (res.ok) {
                    this.$router.push('/Quizes/' + this.cid)
                } else {
                    const errorData = await res.json();
                    alert("Error: " + (errorData.message || "Invalid duration format!"));

                }
            } catch (error) {
                alert("Error: Could not connect to the server.");
                console.log(error)
            }
        }
    },
    async mounted() {
            try {
                const res1 = await fetch('http://localhost:5000/' + 'api/quiz/' + this.quiz_id, {
                    method: 'GET',
                    headers: { 'Content-Type': 'application/json', 'Authentication-Token': JSON.parse(localStorage.getItem('user')).token }
                })
                if (res1.ok) {
                    const quiz = await res1.json()
                    this.remarks = quiz.remarks;
                    this.duration = quiz.duration;

                }
            } catch (error) {
                alert("Error: Could not connect to the server.");
                console.log(error)
            }
        
        },
    

    


}

</script>

<style scoped></style>