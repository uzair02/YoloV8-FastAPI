import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { uploadImage } from '../api';
import './css/HomePage.css'; 

const HomePage = () => {
    const [file, setFile] = useState(null);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(false); 
    const navigate = useNavigate();

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError(null);
        if (!file) {
            setError('Please select a file.');
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        setLoading(true);
        try {
            const results = await uploadImage(formData);
            navigate('/results', { state: { results } });
        } catch (err) {
            setError('Failed to upload image. Please try again.');
        } finally {
            setLoading(false);  
        }
    };

    return (
        <div className="search-page">
            <div className="home-page-content">
                <h1 className="font-bold text-6xl leading-tight text-center mb-8 text-shadow">
                    Find the best deals on <br /> SnapShop
                </h1>
                <p className="text-lg mt-[-8px] mb-4 text-center text-shadow">
                    Where Savings Meet Simplicity – Upload Image!
                </p>
                <form onSubmit={handleSubmit}>
                    <input type="file" accept="image/*" onChange={handleFileChange} />
                    <button type="submit">Search</button>
                    {error && <p className='error-msg'>{error}</p>}
                    {loading && <div className="loader"></div>} {/* Loader */}
                </form>
            </div>
        </div>
    );
};

export default HomePage;
