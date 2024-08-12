import axios from 'axios';

// Create an Axios instance with default settings
const api = axios.create({
    baseURL: 'http://localhost:8000', // Base URL for API requests
});

// Define the API endpoints and their functions
export const uploadImage = async (formData) => {
    try {
        const response = await api.post('/upload/', formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
        });
        return response.data; // Return the data from the response
    } catch (error) {
        console.error("Error uploading image:", error);
        throw error; // Rethrow the error to handle it in the component
    }
};

export const getItems = async () => {
    try {
        const response = await api.get('/items/');
        return response.data; // Return the data from the response
    } catch (error) {
        console.error("Error fetching items:", error);
        throw error; // Rethrow the error to handle it in the component
    }
};
