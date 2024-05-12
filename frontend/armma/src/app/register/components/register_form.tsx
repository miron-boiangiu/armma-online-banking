'use client'

import axios from 'axios';
import { API_REGISTER_URL } from "@/app/utils/api_routes"
import { useState } from 'react';
import { useRouter } from 'next/navigation'

export default function RegisterForm() {
    const [mail, setMail] = useState("");
    const [password, setPassword] = useState("");
    const router = useRouter()

    function handleSubmit() {
        console.log("Register start");

        axios.post(API_REGISTER_URL, { // TODO: Handle existent user error
            username: mail,
            password: password
        }).then((response) => {
            console.log(response)
        });

        console.log("Registered successfully.");

        router.push("/login")
    }

    return (
        <form method="POST">

          <input type="text" placeholder="Enter Email" name="email" id="email" value={mail} onChange={(e) => setMail(e.target.value)} required />
        
          <input type="password" placeholder="Enter Password" name="psw" id="psw" value={password} onChange={(e) => setPassword(e.target.value)} required />
      
          <button onClick={handleSubmit} type="button">Register</button>
      </form>
    )
}