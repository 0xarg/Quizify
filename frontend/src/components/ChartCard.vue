<template>
    <div class="chart-container">
        <canvas ref="canvas"></canvas>
    </div>
</template>

<script>
    import { Chart,registerables } from "chart.js";

    Chart.register(...registerables);
    export default {
        name:'ChartCard',
        props:{
            chartData: { type:Object,required:true },
            chartType: { type:String,default:'bar' },
            chartOptions: {type:Object, default: ()=>({ responsive:true, plugins: { legend :{ display: true }}})}
        },
        mounted(){
            this.chart = new Chart(this.$refs.canvas,{
                type: this.chartType,
                data: this.chartData,
                options: this.chartOptions
            });
        },
        beforeMount(){
            if (this.chart) this.chart.destroy();
        }
    }
</script>

    <style scoped>
    .chart-container {
        width: 100%;
        max-width: 600px;
        margin: auto;
        padding: 1rem;
    }

    canvas {
        max-height: 400px;
    }
</style>
