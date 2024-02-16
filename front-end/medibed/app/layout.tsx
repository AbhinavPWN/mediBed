import type { Metadata } from "next";
import { Merriweather } from "next/font/google";
// import { Lusitana } from "next/font/google";
import "./globals.css";
import Navbar from "./components/Navbar"

// const lusitana = Lusitana({ weight: ['400'],subsets: ["latin"] });
const merriweather = Merriweather({ weight: ['400'],subsets: ["latin"],style:['normal'] });

export const metadata: Metadata = {
  title: "MediBed",
  description: "Find The Available ICU BEDS Near You",
};

export default function RootLayout({children,}: Readonly<{children: React.ReactNode;}>) {

  return (
    <html lang="en">
      <body className={merriweather.className}>
        <Navbar/>
        <main className="lg:mx-24">
          {children}
        </main>
      </body>
    </html>
  );
}
