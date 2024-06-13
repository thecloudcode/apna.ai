import { Button } from "@/components/ui/button"
import Image from "next/image"
import { MapFilterItems } from "./components/MapFilterItems"
import Search from "./components/Search"

export default function Home(){
  return( 
    <div className="container mx-auto px-5 lg:px-10">
      <MapFilterItems/>
    </div>
  )
}