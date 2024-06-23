// import Image from "next/image";
import Hero from "@/components/hero";
// import { FloatingNav } from "@/components/ui/floatingnav";
import { NavbarDemo } from "./components/navbar";
import { InfiniteMovingCardsDemo } from "@/components/cards";
import { AnimatedTooltipPreview } from "@/components/animated-tooltip";
import { CardHoverEffectDemo } from "@/components/cards-companies";
import { FloatingNav } from "@/components/ui/floatingnav";
import Grid from "@/components/Grid";
// import TableDemo from "@/components/table";
// import TableDemo from "./table";
import TableDemo from "./table";
export default function Home(){
  return (
    <main className="relative bg-black flex justify-center items-center flex-col overflow-hidden mx-auto sm:px-10 px-5">
      <div className="max-w-7xl w-full">
        {/* <NavbarDemo/> */}
        <FloatingNav navItems={[{name:'Home', link:'/'}]}/>

        <Hero/>
        <AnimatedTooltipPreview/>
        {/* <TableDemo/> */}
        <CardHoverEffectDemo/>
        <InfiniteMovingCardsDemo/>
      </div>
    </main>
  );
}