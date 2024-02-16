import Link from "next/link";

export default function Logo(){
    return (
        <div className="flex items-center">
            <Link  href='/' className="font-semibold">
                Image logo
            </Link>
        </div>
    );
}