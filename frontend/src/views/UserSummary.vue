<template>
    <div>
        <h1>User Dashboard</h1>
        <ChartCard v-if="quizLabels.length" :chart-data="quizChart" />
        <ChartCard v-if="attemptLabels.length" :chart-data="attemptChart" />
    </div>
</template>

<script>
import { mapState } from 'vuex';
import ChartCard from '@/components/ChartCard.vue';

export default {
    components: { ChartCard },
    props: { userId: { type: Number, required: true } },
    computed: {
        ...mapState('dashboard', ['quizCounts', 'attemptCounts']),
        quizLabels() { return this.quizCounts.map(o => o.subject) },
        attemptLabels() { return this.attemptCounts.map(o => o.subject) },
        quizChart() {
            return { labels: this.quizLabels, datasets: [{ label: 'Total Quizzes', data: this.quizCounts.map(o => o.count), backgroundColor: 'rgba(54,162,235,0.5)' }] };
        },
        attemptChart() {
            return { labels: this.attemptLabels, datasets: [{ label: 'Your Attempts', data: this.attemptCounts.map(o => o.count), backgroundColor: 'rgba(255,206,86,0.5)' }] };
        }
    },
    mounted() {
        this.$store.dispatch('dashboard/fetchUserData', this.userId);
    }
};
</script>
  
