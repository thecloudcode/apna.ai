import { useState } from 'react';
import './App.css';
import axios from "axios";

function App() {
  const [Question, setquestion] = useState("");
  const [Answer, setAnswer] = useState("");

  async function generateAnswer() {
    setAnswer("Loading");

    // Log the API key to check if it's being read correctly
    console.log("API Key:", import.meta.env.VITE_GEMINI_API_KEY);

    try {
      const response = await axios({
        url: `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=${import.meta.env.VITE_GEMINI_API_KEY}`,
        method: "post",
        data: { "contents": [{ "parts": [{ "text": Question }] }] }
      });
      console.log("Response data:", response.data);
      setAnswer(response.data.candidates[0].content.parts[0].text);
    } catch (error) {
      console.error("Error fetching the answer:", error);
      setAnswer("Error fetching the answer");
    }
  }

  return (
    <>
      <h1>Chat Bot</h1>
      <textarea value={Question} onChange={(e) => setquestion(e.target.value)}></textarea>
      <button onClick={generateAnswer}>Answer</button>
      <pre>{Answer}</pre>
    </>
  );
}

export default App;


