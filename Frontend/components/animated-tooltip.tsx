"use client";
import React from "react";
import { AnimatedTooltip } from "./ui/animated-tooltip";
const people = [
  {
    id: 1,
    name: "Badal Prasad Singh",
    designation: "Software Engineer",
    image:
      "https://avatars.githubusercontent.com/u/114615639?v=4",
  },
  {
    id: 2,
    name: "Keerthi K",
    designation: "Data Scientist",
    image:
      "https://avatars.githubusercontent.com/u/113668434?v=4",
  },
  {
    id: 3,
    name: "Yashwanth Sai",
    designation: "Data Scientist",
    image:
      "https://avatars.githubusercontent.com/u/120659244?v=4",
  },
  {
    id: 4,
    name: "Akshaya Vardhini",
    designation: "Data Scientist",
    image:
      "https://avatars.githubusercontent.com/u/119718237?v=4",
  },
  {
    id: 5,
    name: "Bindu Vamsi",
    designation: "Data Scientist",
    image:
      "https://avatars.githubusercontent.com/u/113668417?v=4",
  }
];

export function AnimatedTooltipPreview() {
  return (
    <div className="flex flex-row items-center justify-center my-20 w-full gap-3">
        <h2 className='uppercase tracking-widest text-xs text-center text-blue-100 my-10'>
                CONTRIBUTORS
            </h2>
      <AnimatedTooltip items={people} />
    </div>
  );
}
