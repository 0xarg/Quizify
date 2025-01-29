<template>
    <div>
        <h3>Add Quiz</h3>
        <p>{{ this.sid }}</p>
        <label for="remarks">Remarks: </label>
        <input id="remarks" placeholder="remarks" v-model="remarks" />
        <br>
        <br>
        <label for="duration">Duration: </label>
        <input id="duration" placeholder="Duration"  v-model="duration" />
        <br>
        <br>
        <button @click='AddQuiz'>Add Quiz</button><br>
        
    </div>
</template>

<script>
export default {
    name: 'AddQuiz',
    props:["chapter_id","sid"],
    data() {
        return {
            duration: null,
            name: null,
            remarks: null,
        }
    },
    methods: {
        async AddQuiz() {
            const res = await fetch('http://localhost:5000/' + 'api/quizes/'+this.chapter_id, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ remarks: this.remarks, duration: this.duration})
            })
            if (res.ok) {
                console.log('Valid Chapter')
                const data = await res.json()
                this.$router.push('/Chapters/'+ this.chapter_id)




            }
        }

    },
    mounted() {
        console.log('Add Quiz component mounted');
    },
}
</script>

<style scoped></style>