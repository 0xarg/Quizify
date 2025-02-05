<template>
    <div>
        <br>
        <label >Question Statement: </label>
        <input type="text" v-model="statement"  placeholder="statement">
        <br>
        <br>
        <label >Option 1: </label>
        <input type="text" id="option_1" v-model="option_1" placeholder="Option 1">
        <br>
        <br>
        <label >Option 2: </label>
        <input type="text" id="option_2" v-model="option_2" placeholder="Option 2">
        <br>
        <br>
        <label >Option 3 : </label>
        <input type="text" id="option_3" v-model="option_3" placeholder="Option 3">
        <br>
        <br>
        <label >Option 4: </label>
        <input type="text" id="option_4" v-model="option_4" placeholder="Option 4">
        <br>
        <br>
        <label >Marks for this Question: </label>
        <input type="number" v-model="marks" placeholder="Mark">
        <br>
        <br>
        <label >Correct Option: </label>
        <select v-model="correct_answer" required>
            <option :value="option_1">{{ option_1 || "Option 1" }}</option>
            <option :value="option_2">{{ option_2 || "Option 2" }}</option>
            <option :value="option_3">{{ option_3 || "Option 3" }}</option>
            <option :value="option_4">{{ option_4 || "Option 4" }}</option>
        </select>
        <hr>
        <button @click='AddQuestion'>Add</button>

    </div>
</template>

<script>
export default {
    name: "AddQuestion",
    props: ["quiz_id"],
        data() {
        return {


            statement: null,
            option_1: null,
            option_2: null,
            option_3: null,
            option_4: null,
            correct_answer: null,
            marks: null,

        }
    },
    methods: {
        async AddQuestion() {
            try {
                const res = await fetch('http://localhost:5000/' + 'api/question/' + this.quiz_id, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json', 'Authentication-Token': JSON.parse(localStorage.getItem('user')).token },
                    body: JSON.stringify({ statement: this.statement, option_1: this.option_1, option_2: this.option_2, option_3: this.option_3, option_4: this.option_4, correct_answer: this.correct_answer, marks:this.marks })
                })
                if (res.ok) {
                    const data = await res.json()
                    this.$router.push('/Quiz/' + this.quiz_id)
                } else {
                    const errorData = await res.json();
                    alert("Error: " + (errorData.message || "Invalid Input"));

                }
            } catch (error) {
                alert("Error: Could not connect to the server.");
                console.log(error)
            }
        }
    }
}
</script>

<style scoped></style>