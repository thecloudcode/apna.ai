import Link from "next/link"
import Image from "next/image"
import DesktopLogo from '../../public/apna-logo.png'
import AI from '../../public/ai-generate.png'
import { UserNav } from "./UserNav"

export function Navbar() {
    return(
        <nav className="w-full border-b">
            <div className="flex items-center justify-between container mx-auto px-5 lg:px-10 py-5">
                <Link href="/">
                    <Image src={DesktopLogo}
                    alt="Desktop Logo"
                    className="w-[70px] hidden lg:block"
                />
                    {/* <Image src={MobileLogo} */}
                    {/* alt="Mobile Logo" */}
                    {/* className="block lg:hidden w-32" */}
                    {/* /> */}
                </Link>
                <div className="flex justify-end rounded-full items-center border px-5 py-2 w-[50%]">
                    <p>Let <b>AI</b> Search you a Job </p>
                    <Image src={AI}
                    alt="AI"
                    className="mx-2 w-7"
                    />
                </div>
                <UserNav />
            </div>
        </nav>
    )
}