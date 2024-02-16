const AvailableBeds = () => {
    
    let b:number = 65;  

  return (
    <div className="relative top-4 border-2 rounded-lg bg-slate-300    h-20">
        <div className="absolute mt-2 px-8 ">
            <h1 className="">ICU Beds available</h1>
        </div>
        <div className="absolute mt-10 px-8">
            <h1> {70} </h1>
        </div>
    </div>
  )
}

export default AvailableBeds