"use client";
import React, { useState } from 'react';
import { PlaceholdersAndVanishInput } from '@/components/ui/placeholder';
import {
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
  } from "@/components/ui/card"
import { BackgroundBeams } from '@/components/ui/backgroundbeams';

interface apnaaiagents {}

const ChatGPTInterface: React.FC<apnaaiagents> = () => {
  const [input, setInput] = useState('');
  const [response, setResponse] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await fetch('http://127.0.0.1:8000/agents', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: input }),
      });
      const data = await res.json();
      setResponse(data);
    } catch (error) {
      console.error('Error fetching data:', error);
    } finally {
      setLoading(false);
    }
  };

  const placeholders = [
    "What are the most trending job roles in the market?",
    "Which job pays the highest?",
    "Do companies take freshers as Data Scientist?",
    "Will AI take our jobs?",
    "Which company hires the most?",
  ];

  const onSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    console.log("submitted");
  };

  return (
    <>
    <div className="p-10 h-full bg-black flex flex-col justify-center  items-center px-4">
        <h2 className="mt-40 mb-10 sm:mb-20 text-xl text-center sm:text-5xl dark:text-white text-black">
            <b>apna.ai</b> agents
        </h2>
        <PlaceholdersAndVanishInput
            placeholders={placeholders}
            onChange={(e) => setInput(e.target.value)}
            onSubmit={handleSubmit}
        />
        <button
          type="submit"
          className="mt-10 bg-neutral-950 hover:bg-neutral-950 text-white font-bold py-2 px-4 rounded"
          disabled={loading}
        >
          {loading ? 'Loading...' : ''}
        </button>

        {response && (<>
        <Card className="w-[550px] bg-neutral-950 border-black">
            <CardHeader>
                <CardTitle>✍🏻 Google Researcher</CardTitle>
                
                <CardDescription>
                    <pre className="whitespace-pre-wrap mt-4">{response["Google Researcher"]}</pre>
                </CardDescription>
            </CardHeader>
        </Card>
        <Card className="w-[550px] bg-neutral-950 border-black">
            <CardHeader>
                <CardTitle>🕵️‍♂️ Data Scientist</CardTitle>
                <CardDescription>
                    <pre className="whitespace-pre-wrap mt-4">{response["Data Scientist Researcher"]}</pre>
                </CardDescription>
            </CardHeader>
        </Card>
        <Card className="w-[550px] bg-neutral-950 border-black">
            <CardHeader>
                <CardTitle>👨‍💻 Software Engineer</CardTitle>
                
                <CardDescription>
                    <pre className="whitespace-pre-wrap mt-4">{response["Software Engineer Researcher"]}</pre>
                </CardDescription>
            </CardHeader>
        </Card></>)}
              <BackgroundBeams />
              
    </div>
    </>
  );
};

export default ChatGPTInterface;
