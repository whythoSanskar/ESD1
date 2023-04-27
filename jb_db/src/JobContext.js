import react, { useState, createContext } from 'react'

export const JobContext = createContext();

export const JobProvider = (props) =>{
    const [jobs, products] = useState({"data":[]});

    return (
        <JobContext.Provider value={[jobs, products]}>
            {props.chilren}
        </JobContext.Provider>
    )
}