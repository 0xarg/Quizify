<template>
    <div>
        <h1>{{ subject.name }}</h1>
        <hr>
        <h4>{{ subject.description }}</h4>

        <button @click = "$router.push('/AddChapter/'+ subject.id)"> Add Chapter </button>
        <hr>
        <button @click = "$router.push('/Chapters/'+ subject.id)"> View Chapters </button>
        

    </div>
</template>

<script>
    export default {
        name: 'SubjectDisplay',
        props: ["id"],
        data() {
            return {
                subject:[]
            }
        },
        async mounted() {
            const res = await fetch('http://localhost:5000/' + '/api/subjects/' + this.id,{
                headers: {
                    'Authentication-Token': JSON.parse(localStorage.getItem('user')).token
                }
            })
            if (res.ok){
                this.subject = await res.json()
            }else{
                alert('Subject not Found')
                this.$router.push('/api/subjects/')
            }

        }
    }
</script>

<style scoped>

</style>