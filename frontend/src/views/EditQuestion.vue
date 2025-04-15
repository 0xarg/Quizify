<template>
    <div>
        <br>
        <label >Question Statement: </label>
        <input type="text" v-model="statement"  placeholder="statement" value="990">
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
        <button @click='EditQuestion'>Edit✅</button>

    </div>
</template>

<script>
export default {
    name: "EditQuestion",
    props: ["question_id","quiz_id"],
        data() {
        return {

            statement: "",
            option_1:"",
            option_2:"",
            option_3:"",
            option_4:"",
            correct_answer:"",
            marks: null
          

        }
    },
    methods: {
        async EditQuestion(){
            try {
                const res = await fetch('http://localhost:5000/' + 'api/question/' + this.question_id, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json', 'Authentication-Token': JSON.parse(localStorage.getItem('user')).token },
                    body: JSON.stringify({ statement: this.statement, option_1: this.option_1, option_2: this.option_2, option_3: this.option_3, option_4: this.option_4, correct_answer: this.correct_answer, marks:this.marks })
                })
                if (res.ok) {
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
    },
    async mounted() {
            try {
                const res1 = await fetch('http://localhost:5000/' + 'api/question/' + this.question_id, {
                    method: 'GET',
                    headers: { 'Content-Type': 'application/json', 'Authentication-Token': JSON.parse(localStorage.getItem('user')).token }
                })
                if (res1.ok) {
                    const question = await res1.json()
                    this.statement = question.statement;
                    this.option_1 = question.options[0];
                    this.option_2 = question.options[1];
                    this.option_3 = question.options[2];
                    this.option_4 = question.options[3];
                    this.correct_answer = question.correct_answer;
                    this.marks = question.marks;

                }
            } catch (error) {
                alert("Error: Could not connect to the server.");
                console.log(error)
            }
        
    
}
}
</script>

<style scoped></style>