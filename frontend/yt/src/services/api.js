import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api/downloader/'; // Django backend URL

export const downloadVideo = async (url) => {
    try {
        const response = await axios.post(`${API_URL}download/`, { url });
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
};
