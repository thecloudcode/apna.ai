import { DropdownMenuTrigger, DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuSeparator } from "@/components/ui/dropdown-menu";
import { MenuIcon } from "lucide-react";
import {RegisterLink, LoginLink, LogoutLink} from "@kinde-oss/kinde-auth-nextjs/components";
import { getKindeServerSession } from "@kinde-oss/kinde-auth-nextjs/server";
import Link from "next/link";
import { createAirbnbHome } from "../actions";

export async function UserNav() {
    const {getUser} = getKindeServerSession();
    const user = await getUser();

    const createHomewithId = createAirbnbHome.bind(null, {userId: user?.id as string,});
    return(
        <DropdownMenu>
            <DropdownMenuTrigger>
                <div className="rounded-full border px-2 py-2 lg:px-4 flex items-center gap-x-3">
                    <MenuIcon className="w-6 h-6 lg:w-5 lg:h-5"/>
                    <img src={user?.picture??"https://thumbs.dreamstime.com/b/default-avatar-profile-icon-vector-social-media-user-image-182145777.jpg"}
                    alt="Image of User"
                    className="rounded-full h-8 w-8 lg:block"/>
                </div>
            </DropdownMenuTrigger>
            <DropdownMenuContent align="end" className="w-[200px]">
                {user? (<>
                    <DropdownMenuItem>
                        <form action={createHomewithId} className="w-full">
                            <button type="submit" className="w-full text-start">
                                Dashboard
                            </button>
                        </form>
                    </DropdownMenuItem>
                    <DropdownMenuItem>
                        <Link href="/my-homes" className="w-full">
                            Profile
                        </Link>
                    </DropdownMenuItem>
                    <DropdownMenuItem>
                        <Link href="/my-homes" className="w-full">
                            Applications
                        </Link>
                    </DropdownMenuItem>
                    <DropdownMenuItem>
                        <Link href="/my-homes" className="w-full">
                            Favourites
                        </Link>
                    </DropdownMenuItem>
                    <DropdownMenuSeparator/>
                    <DropdownMenuItem>
                        <LogoutLink className="w-full">Logout</LogoutLink>
                    </DropdownMenuItem>
                    </>): (<>
                    <DropdownMenuItem><RegisterLink className="w-full">Register</RegisterLink></DropdownMenuItem>
                    <DropdownMenuItem><LoginLink className="w-full">Login</LoginLink></DropdownMenuItem>
                    </>
                )}
            </DropdownMenuContent>
        </DropdownMenu>
    )
}