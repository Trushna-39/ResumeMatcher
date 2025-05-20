import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [resumeFile, setResumeFile] = useState(null);
  const [jobDescription, setJobDescription] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleResumeChange = (e) => {
    setResumeFile(e.target.files[0]);
  };

  const handleDescriptionChange = (e) => {
    setJobDescription(e.target.value);
  };

  const handleSubmit = async () => {
    if (!resumeFile || !jobDescription.trim()) {
      alert("Please upload a resume and enter a job description.");
      return;
    }

    const formData = new FormData();
    formData.append('resume', resumeFile);
    formData.append('jd', jobDescription);

    try {
      setLoading(true);
      const response = await axios.post('/analyze', formData); // ← proxy handles the rest
      setResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Error analyzing resume. Check backend is running.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial" }}>
      <h2>Resume Matcher</h2>
      <input type="file" accept=".pdf" onChange={handleResumeChange} /><br /><br />
      <textarea
        placeholder="Paste job description here..."
        value={jobDescription}
        onChange={handleDescriptionChange}
        rows={10}
        style={{ width: "100%" }}
      ></textarea><br /><br />
      <button onClick={handleSubmit}>Analyze</button>

      {loading && <p>Analyzing...</p>}

      {result && (
        <div style={{ marginTop: "2rem" }}>
          <h3>Matched Keywords:</h3>
          <ul>{result.matched_keywords.map(k => <li key={k}>{k}</li>)}</ul>

          <h3>Missing Keywords:</h3>
          <ul>{result.missing_keywords.map(k => <li key={k}>{k}</li>)}</ul>

          <h3>Score:</h3>
          <p>{result.score}%</p>
        </div>
      )}
    </div>
  );
}

export default App;
