import Image from "next/image"

const Hero = () => {
  return (
    <div className="relative top-2  flex justify-center items-center h-48 rounded-lg overflow-hidden">
        <div className="absolute top-0 left-0 w-full ">
            <Image src={'/hero.webp'} alt="Hero Image"  className="rounded-lg" height={270} width={1500} priority/>
            <div className="bg-black opacity-50 w-full h-full absolute top-0 left-0"></div>
        </div>
        <div className="z-8 text-white text-center absolute lg:top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
            <h1 className="text-lg lg:text-4xl text-bold">Find an ICU Bed around You</h1>
            <div className="mx-auto max-w-lg lg:max-w-none">  
                <input type="text" placeholder="Search for hospitals or services... " className="px-4 py-2 w-full rounded-md border-none shadow-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-black" />
            </div>
        </div>
    </div>
  )
}

export default Hero