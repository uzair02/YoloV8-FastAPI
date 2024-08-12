import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Homepage from './pages/HomePage';
import ResultsPage from './pages/ResultsPage';
import './App.css'

function App() {

  return (
    <Router>
      <Routes>
        <Route path='/' element={<Homepage />} />
        <Route path='/results' element={<ResultsPage />} />
      </Routes>
    </Router>
  );
};

export default App;
