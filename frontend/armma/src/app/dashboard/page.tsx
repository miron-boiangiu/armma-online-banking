'use client'

import axios from 'axios';
import { useRouter } from 'next/navigation'
import { useEffect, useState } from 'react';
import { API_USER_INFO_URL } from '../utils/api_routes';

interface userDataInterface {
    id: number,
    is_admin: number,
    username: string
}

export default function Dashboard() { // Inaccessible if user is not logged in
    const [userData, setUserData]= useState<userDataInterface | null>(null)
    const router = useRouter()

    useEffect(() => {
        // Check that we have a token 
        // TODO: Check if the token is still valid.
        
        if (localStorage.getItem("token") === null) {
            router.push("/login")
            return;
        }
    
        const token = localStorage.getItem("token")

        console.log(token)  // TODO: Unsafe log

        axios.get(API_USER_INFO_URL, { headers: {"Authorization" : `Bearer ${token}`} })
        .then((response) => (userData === null) && setUserData(response.data.message))
    })

    if (userData === null) {
        return "Haven't fetched data yet"
    }

    return (
        <div>
            Dashboard
            <br />
            You are {userData.username}
            <button onClick={() => {
                localStorage.removeItem("token")
                router.push("/login")
                }}> Log out </button>
        </div>
    )
}