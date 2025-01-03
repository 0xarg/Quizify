<template>
    <div>
        <p>{{ msg }}</p>
    </div>
</template>

<script>
export default {
    name: 'Ping',
    data() {
        return {
            msg: '',
        };
    },
    methods: {
        async getMessage() {
            const path = 'http://localhost:5000/ping';
            try {
                const response = await fetch(path);
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();
                this.msg = data;
            } catch (error) {
                console.error(error);
            }
        },
    },
    created() {
        this.getMessage();
    },
};
</script>




