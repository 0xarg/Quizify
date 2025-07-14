<template>
    <div>
        <h1>Admin Dashboard</h1>
        <ChartCard v-if="labelsScores.length" :chart-data="topScoresChart" />
        <ChartCard v-if="totalUsers !== null" :chart-data="userCountChart" chart-type="doughnut" />
    </div>
</template>

<script>
import { mapState } from 'vuex';
import ChartCard from '@/components/ChartCard.vue';

export default {
    components: { ChartCard },
    computed: {
        ...mapState('dashboard', ['topScores', 'totalUsers']),
        labelsScores() { return this.topScores.map(o => o.subject) },
        topScoresChart() {
            return {
                labels: this.labelsScores,
                datasets: [{ label: 'Top Scores', data: this.topScores.map(o => o.top_score), backgroundColor: 'rgba(75,192,192,0.5)' }]
            };
        },
        userCountChart() {
            return {
                labels: ['Users'],
                datasets: [{ label: 'Total Users', data: [this.totalUsers], backgroundColor: ['rgba(255,99,132,0.5)'] }]
            };
        }
    },
    mounted() {
        this.$store.dispatch('dashboard/fetchAdminData');
    }
};
</script>
  
