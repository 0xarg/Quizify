<template>
    <div>
        <h3>Add Quiz</h3>
        <p>{{ this.sid }}</p>
        <label for="remarks">Remarks: </label>
        <input id="remarks" placeholder="remarks" v-model="remarks" />
        <br>
        <br>
        <label for="duration">Duration:(HH:MM:SS) </label>
        <input id="duration" placeholder="HH:MM:SS" v-model="duration" />
        <br>
        <br>
        <button @click='AddQuiz'>Add Quiz</button><br>

    </div>
</template>

<script>
import VueTimepicker from 'vue3-timepicker'
export default {
    name: 'AddQuiz',
    props: ["chapter_id", "sid"],
    data() {
        return {
            duration: null,
            name: null,
            remarks: null,
        }
    },
    methods: {
        async AddQuiz() {
            try {
                const res = await fetch('http://localhost:5000/' + 'api/quizes/' + this.chapter_id, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authentication-Token': JSON.parse(localStorage.getItem('user')).token},
                    body: JSON.stringify({ remarks: this.remarks, duration: this.duration })
                })
                if (res.ok) {
                    const data = await res.json()
                    this.$router.push('/Chapters/' + this.chapter_id)
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
mounted() {
    console.log('Add Quiz component mounted');
},
}

</script>

<style scoped></style>