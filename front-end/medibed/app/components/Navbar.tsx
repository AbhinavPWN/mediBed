import Logo from "./Logo";
import Login from "./Login";
import NavigationLinks from "./Navigation";

interface NavigationLink {
  name: string;
  href: string;
}

const navigation: NavigationLink[] = [
  { name: 'About', href: '#' },
  { name: 'Contact', href: '#' },
  { name: 'Hospital', href: '#' },
  { name: 'Ambulance', href: '#' },
];

export default function Navbar() {
  return (
    <>
    <header className="lg:flex relative top-0 flex   w-full items-center justify-between px-4 py-6 border-b border-gray-500">
        <Logo />
        <NavigationLinks navigation={navigation} />
        <Login />
    </header>
    <hr />
    </>
    
  
  );
}