<template>
    <div class="dashboard-container">
        <Sidebar />

        <div class="content">
            <h1>Admin Dashboard</h1>

            <ChartCard v-if="topScoresChart.labels.length" :chart-data="topScoresChart" />

            <ChartCard v-if="attemptsChart.labels.length" :chart-data="attemptsChart" />
        </div>
    </div>
</template>

<script>
import { mapState } from 'vuex';
import ChartCard from '@/components/ChartCard.vue';
import Sidebar from '@/components/sidebar.vue';

export default {
    components: { ChartCard,Sidebar },
    computed: {
        ...mapState('dashboard', ['topScores', 'subjectAttempts']),

        topScoresChart() {
            const scores = Array.isArray(this.topScores) ? this.topScores : [];
            return {
                labels: scores.map(o => o.subject),
                datasets: [{
                    label: 'Top Scores',
                    data: scores.map(o => o.top_score),
                    backgroundColor: 'rgba(75,192,192,0.5)'
                }]
            };
        },

        attemptsChart() {
            const attempts = Array.isArray(this.subjectAttempts) ? this.subjectAttempts : [];
            return {
                labels: attempts.map(a => a.subject),
                datasets: [{
                    label: 'User Attempts by Subject',
                    data: attempts.map(a => a.attempts),
                    backgroundColor: 'rgba(255,159,64,0.6)'
                }]
            };
        }
    },
    mounted() {
        this.$store.dispatch('dashboard/fetchAdminData');
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