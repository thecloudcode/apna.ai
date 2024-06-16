"use client"

import { useState, useRef } from 'react';
import axios from 'axios';

export default function Home() {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [result, setResult] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const fileInputRef = useRef<HTMLInputElement | null>(null);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setSelectedFile(e.target.files[0]);
      setResult(null); // Clear previous result when a new file is selected
    }
  };

  const handleUpload = async () => {
    if (!selectedFile) return;

    const formData = new FormData();
    formData.append('resume', selectedFile);

    setLoading(true);
    try {
      const response = await axios.post('http://localhost:5000/upload', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      setResult(`Score: ${response.data.parse}`);
    } catch (error) {
      setResult('Upload failed. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleButtonClick = () => {
    if (fileInputRef.current) {
      fileInputRef.current.click();
    }
  };

  return (
    <div style={{ display: 'flex', padding: '20px' }}>
      <div style={{ flex: 1 }}>
        {/* Hidden file input */}
        <input
          type="file"
          ref={fileInputRef}
          style={{ display: 'none' }}
          onChange={handleFileChange}
        />
        {/* Custom button */}
        <button 
          onClick={handleButtonClick}
          className="p-2 border bg-blue-500 text-white"
        >
          {selectedFile ? selectedFile.name : 'Choose File'}
        </button>
        <button 
          onClick={handleUpload} 
          disabled={loading || !selectedFile}
          className={`p-2 ml-2 border ${loading ? 'bg-gray-400' : 'bg-blue-500'} text-white`}
        >
          {loading ? 'Uploading...' : 'Upload Resume'}
        </button>
      </div>
      <div style={{ flex: 1, paddingLeft: '20px' }}>
        <h3>Result:</h3>
        <div>{result}</div>
      </div>
    </div>
  );
}
