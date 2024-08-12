import React, { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';
import { getItems } from '../api'; // Import the API function
import './css/ResultsPage.css'; // Import the CSS file

const ResultsPage = () => {
    const location = useLocation();
    const [results, setResults] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        if (location.state && location.state.results) {
            setResults(location.state.results);
        } else {
            const fetchItems = async () => {
                try {
                    const data = await getItems();
                    setResults(data);
                } catch (err) {
                    setError('Failed to fetch items. Please try again.');
                    console.error('Fetch error:', err);
                }
            };

            fetchItems();
        }
    }, [location.state]);

    return (
        <div className="results-page">
            <h1>Search Results</h1>
            {error && <p>{error}</p>}
            <div className="results-container">
                {results.map((item) => (
                    <div className="result-card" key={item.items_id}>
                        <h2>{item.title}</h2>
                        <a href={item.link} target="_blank" rel="noopener noreferrer">
                            {item.link}
                        </a>
                        <p>{new Date(item.timestamp).toLocaleString()}</p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default ResultsPage;
