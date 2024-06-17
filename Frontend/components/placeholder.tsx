"use client";

import React, { useState } from "react";
import axios from "axios";
import { PlaceholdersAndVanishInput } from "./ui/placeholder";

export function PlaceholdersAndVanishInputDemo() {
  const placeholders = [
    "What are the ongoing Market Trends?",
    "Which job role pays a lot?",
    "How can I be an AI Developer?",
    "How much Badal loves programming?",
    "Which companies are hiring Freshers?",
  ];

  const [inputValue, setInputValue] = useState("");
  const [loading, setLoading] = useState(false);
  const [response, setResponse] = useState("");

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setInputValue(e.target.value);
  };

  const onSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setLoading(true);
    setResponse("");

    try {
      // Simulate a delay for the request
      await new Promise((resolve) => setTimeout(resolve, 230000));

      const res = await axios.post("https://gogemini.onrender.com/generate", {
        prompt: inputValue,
        
      });
      console.log(inputValue);
      // Simulate a delay for processing the response
      await new Promise((resolve) => setTimeout(resolve, 2000));

      setResponse(res.data);
    } catch (error) {
      setResponse("An error occurred while fetching the response.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-[15rem] flex flex-col justify-center items-center px-4">
      <h2 className="mb-10 sm:mb-20 text-xl text-center sm:text-5xl dark:text-white text-black">
        Ask Apna-AI Anything
      </h2>
      <PlaceholdersAndVanishInput
        placeholders={placeholders}
        onChange={handleChange}
        onSubmit={onSubmit}
      />
      <div className="mt-4 mb-40">
        {loading ? (
          <p className="text-lg text-center text-gray-500 animate-pulse">
            Waiting for the response...
          </p>
        ) : (
          response && <p className="text-lg text-center text-gray-800 dark:text-gray-200">{response}</p>
        )}
      </div>
    </div>
  );
}
