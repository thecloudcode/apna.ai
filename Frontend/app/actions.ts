"use server"


import { redirect } from "next/navigation";
import prisma from "./lib/db"

export async function createAirbnbHome({userId}:{userId: string}){
    const data = await prisma.home.findFirst({
        where: {
            userId: ""
        },
        orderBy: {
            createdAT: "desc",
        }
    });

    if(data===null){
        const data = await prisma.home.create({
            data: {
                userId: userId,
            },
        });

        return redirect('/create/${data.id}/structure');
    }else if(!data.addedCateroy && !data.addedDescription && !data.addedLocation){
        return redirect('/create/${data.id}/structure');
    }else if(data.addedCateroy && !data.addedDescription){
        return redirect('/create/${data.id}/description');
    }
}

// export asnyc function createCategoryPage(formData: FormData){

// }