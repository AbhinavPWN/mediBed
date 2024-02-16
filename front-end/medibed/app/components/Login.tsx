import React from 'react';
import Link from 'next/link';

const Login = () => {
  return (
    <div className='lg:flex items-center justify-around space-x-4 hidden'>
    <Link href="/" className="text-gray-900 hover:bg-gray-600 hover:text-slate bg-transparent hover:text-slate-100">
      Sign up
    </Link>
    <Link href="/" className="text-gray-900 hover:bg-gray-600 hover:text-slate bg-transparent hover:text-slate-100 ">
      Log in
    </Link>
    </div>
  );
};

export default Login;