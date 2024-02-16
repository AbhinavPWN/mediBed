'use client'

import React from 'react';
import Link from 'next/link';
import { useState } from 'react';
import Image from 'next/image';

interface NavigationLink {
  name: string;
  href: string;
}

const NavigationLinks= ({
  navigation,}: {navigation: NavigationLink[]}
) => {

  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  }

  return (
    <div>
    <button 
    className='block lg:hidden text-white focus:outline-indigo-400'
    onClick={toggleMenu}
    >
    {isMenuOpen ? (
          <Image src='/close.svg' alt="Close Icon" width={24} height={24} />
        ) : (
          <Image src='/menu.svg' alt="Menu Icon" width={24} height={24} />
        )}
    </button>

{/* Nav links dropdown */}
{ isMenuOpen && (
  <div className='lg:hidden absolute top-16 left-0 w-full z-10 py-4 opacity-80 bg-white rounded-md '>
          <ul className='flex flex-col items-center'>
          {navigation.map((item,index) => (
          <li key={item.name} className={`mb-4 ${index !== 0 ? 'mt-4' : ''}`}>
            <Link href={item.href} className="text-black text-xl  hover:text-2xl  py-2 capitalize font-medium">
              {item.name}
            </Link>
            <div className="border-t border-gray-600 mt-2"></div>
          </li>
        ))}
        <li>
            <Link href={'/'} className="text-black hover:text-2xl   py-2 capitalize font-medium text-xl"> Log in </Link>
            <div className="border-t border-gray-600 mt-2"></div>
        </li>
        
    </ul>

  </div>
)}


{/* Navbar for large devices */}
<nav className="hidden lg:flex text-center lg:items-center lg-space-x-6">
  <ul className="flex space-x-4 justify-center flex-col lg:flex-row lg:items-center space-y-4 lg:space-y-0">
    {navigation.map((item) => (
    <li key={item.name}>
      <Link href={item.href} className="text-gray-900 hover:bg-gray-50  capitalize">
        {item.name}
      </Link>
    </li>
  ))}
</ul>
</nav>
    </div>
  );
};

export default NavigationLinks;