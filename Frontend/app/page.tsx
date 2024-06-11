import Image from "next/image";
import Hero from "@/components/hero";
import { FloatingNav } from "@/components/ui/floatingnav";
import { InfiniteMovingCardsDemo } from "@/components/cards";
import { AnimatedTooltipPreview } from "@/components/animated-tooltip";
import { CardHoverEffectDemo } from "@/components/cards-companies";
export default function Home(){
  return (
    <main className="relative bg-black flex justify-center items-center flex-col overflow-hidden mx-auto sm:px-10 px-5">
      <div className="max-w-7xl w-full">
        <FloatingNav navItems={[{name:'Home', link:'/'},{name:'Resume Ranker', link:'https://badal-resume-ranker.streamlit.app/'},{name:'Resume AI',link:'https://chatwithresume.streamlit.app/'},{name:'Chatbot',link:'https://chatbot-lac-ten.vercel.app/'}]}/>
        <Hero/>
        <AnimatedTooltipPreview/>
        <CardHoverEffectDemo/>
        <InfiniteMovingCardsDemo/>
      </div>
    </main>
  );
}