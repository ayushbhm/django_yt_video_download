<template>
    <div>
        <h1>YouTube Video Downloader</h1>
        <input v-model="videoUrl" placeholder="Enter YouTube video URL" />
        <button @click="download">Download Video</button>
        <p v-if="message">{{ message }}</p>
        <p v-if="error" style="color: red;">{{ error }}</p>
    </div>
</template>

<script>
import { ref } from 'vue';
import { downloadVideo } from '../services/api';

export default {
    setup() {
        const videoUrl = ref('');
        const message = ref('');
        const error = ref('');

        const download = async () => {
            message.value = '';
            error.value = '';
            try {
                const response = await downloadVideo(videoUrl.value);
                message.value = response.message;
            } catch (err) {
                error.value = err.error || 'An error occurred';
            }
        };

        return {
            videoUrl,
            message,
            error,
            download,
        };
    },
};
</script>

<style scoped>

</style>