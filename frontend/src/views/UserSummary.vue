<template>
    <div class="dashboard-container">
        <Sidebar />

        <div class="content">
            <h1>User Summary</h1>
            <ChartCard v-if="subjectWiseQuizChart.labels.length" :chart-data="subjectWiseQuizChart" chart-type="bar" />
            <ChartCard v-if="monthlyAttemptsChart.labels.length" :chart-data="monthlyAttemptsChart" chart-type="pie" />
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import ChartCard from '@/components/ChartCard.vue';
import Sidebar from '@/components/sidebar.vue';

export default {
    components: { ChartCard, Sidebar },
    data() {
        return {
            quizStats: { quizCount: [], attemptCount: [] },
            userId: null // Set dynamically or from store/token
        };
    },
    computed: {
        subjectWiseQuizChart() {
            const data = this.quizStats.quizCount;
            return {
                labels: data.map(d => d.subject),
                datasets: [{
                    label: 'No. of Quizzes',
                    data: data.map(d => d.count),
                    backgroundColor: 'rgba(153,102,255,0.6)'
                }]
            };
        },
        monthlyAttemptsChart() {
            const data = this.quizStats.attemptCount;
            const monthLabels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
            return {
                labels: data.map(d => monthLabels[d.month - 1]),
                datasets: [{
                    label: 'Quiz Attempts',
                    data: data.map(d => d.count),
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.5)',
                        'rgba(54, 162, 235, 0.5)',
                        'rgba(255, 206, 86, 0.5)',
                        'rgba(75, 192, 192, 0.5)',
                        'rgba(153, 102, 255, 0.5)',
                        'rgba(255, 159, 64, 0.5)',
                        'rgba(199, 199, 199, 0.5)',
                        'rgba(83, 102, 255, 0.5)',
                        'rgba(255, 99, 71, 0.5)',
                        'rgba(60, 179, 113, 0.5)',
                        'rgba(123, 104, 238, 0.5)',
                        'rgba(0, 255, 255, 0.5)',
                    ]
                }]

            };
        }
    },
    mounted() {
        this.userId = this.$store.state.user_id; 
        console.log(this.userId)
        axios.get(`http://localhost:5000/api/user/${this.userId}/quiz-stats`)
            .then(res => this.quizStats = res.data)
            .catch(err => console.error(err));
    }
};
</script>
<style scoped>
.dashboard-container {
    display: flex;
}

.content {
    flex: 1;
    padding: 2rem;
}

h1 {
    text-align: center;
}
</style>

