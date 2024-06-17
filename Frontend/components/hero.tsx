import React from 'react'
import { Spotlight } from './ui/Spotlight'
import { TextGenerateEffect } from './ui/text-generate'
import { FlipWords } from './ui/flip-words'
import { SparklesCore } from "./ui/sparkles";
import Magicbutton from './ui/magicbutton';

const hero = () => {
    const words = ["#created-by-Badal", "#a-hiring-website"];

  return (
      <div className="pb-20 pt-36">
        <div>
            <Spotlight className="-top-40 -left-10 md:-left-32 md:-top-20 h-screen" fill="white"/>
            <Spotlight className="top-10 left-full h-[80vh] w-[50vw]" fill="grey"/>
            <Spotlight className="top-28 left-80 h-[80vh] w-[50vw]" fill="blue"/>
        </div>

        

        <div className="h-[20rem] w-full bg-black flex flex-col items-center justify-center overflow-hidden rounded-md">
        <h1 className="md:text-7xl text-3xl lg:text-9xl font-bold text-center text-white relative z-20">
            apna.ai
        </h1>
        <div className="h-[40rem] flex justify-center items-center px-4">
        <div className="text-4xl mx-auto font-normal text-neutral-600 dark:text-neutral-400">
            <FlipWords words={words} ></FlipWords>
        </div>
        </div>
        <div className="w-[40rem] h-40 relative">
            {/* Gradients */}
            <div className="absolute inset-x-20 top-0 bg-gradient-to-r from-transparent via-indigo-500 to-transparent h-[2px] w-3/4 blur-sm" />
            <div className="absolute inset-x-20 top-0 bg-gradient-to-r from-transparent via-indigo-500 to-transparent h-px w-3/4" />
            <div className="absolute inset-x-60 top-0 bg-gradient-to-r from-transparent via-sky-500 to-transparent h-[5px] w-1/4 blur-sm" />
            <div className="absolute inset-x-60 top-0 bg-gradient-to-r from-transparent via-sky-500 to-transparent h-px w-1/4" />

            {/* Core component */}
            <SparklesCore
            background="transparent"
            minSize={0.4}
            maxSize={1}
            particleDensity={1200}
            className="w-full h-full"
            particleColor="#FFFFFF"
            />

            {/* Radial Gradient to prevent sharp edges */}
            <div className="absolute inset-0 w-full h-full bg-black [mask-image:radial-gradient(350px_200px_at_top,transparent_20%,white)]"></div>

        </div>
        </div>
        <div className="h-40 w-full dark:bg-black bg-black  dark:bg-grid-white/[0.03] bg-grid-black/[0.2] relative flex items-center justify-center">
        {/* Radial gradient for the container to give a faded look */}
        <div className="absolute pointer-events-none inset-0 flex items-center justify-center dark:bg-black bg-black [mask-image:radial-gradient(ellipse_at_center,transparent_20%,black)]"></div>
        <p className="text-4xl sm:text-7xl font-bold relative z-20 bg-clip-text text-transparent bg-gradient-to-b from-neutral-200 to-neutral-500 py-8">
            
      </p>
      <div className='flex justify-center my-10'>
        <div className='max-w-[89vw] md:max-w-2xl lg:max-w-[60vw] flex:flex-col items-center my-10'>
            <h2 className='uppercase tracking-widest text-xs text-center text-blue-100 my-10'>
                TRY SOME OF OUR FEATURES
            </h2>

            {/* <TextGenerateEffect
                className="text-center text-[10px] md:text-2xl lg:text-3xl my-1"
                words="We build the bridge between employers and applicants"
            /> */}

            {/* <p className="text-center my-10">Upload your Resume, and find out the top picks for you</p> */}

            <div className='flex gap-5'>
            <a href='https://badal-resume-ranker.streamlit.app/'>
                <Magicbutton title="Resume Ranker"/>
            </a>
            <a href='https://chatwithresume.streamlit.app/'>
                <Magicbutton title="Resume-AI"/>
            </a>
            <a href='https://chatbot-lac-ten.vercel.app/'>
                <Magicbutton title="Chatbot"/>
            </a>

            </div>
        </div>
        
      </div>
      
    </div>
      </div>
      
  )
}

export default hero
