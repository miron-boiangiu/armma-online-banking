'use client'

import axios from 'axios';
import { API_LOGIN_URL } from "@/app/utils/api_routes"
import { useState } from 'react';
import { useRouter } from 'next/navigation'

export default function LoginForm() {
    const [mail, setMail] = useState("");
    const [password, setPassword] = useState("");  // This is not ok
    const router = useRouter()

    function handleSubmit() {
        console.log("Login start");

        axios.post(API_LOGIN_URL, { // TODO: Handle incorrect user/password error
            username: mail,
            password: password
        }).then((response) => {
            console.log(response.data.access_token)  // TODO: Unsafe log

            localStorage.setItem("token", response.data.access_token)
            
            console.log("Logged in successfully.");

            router.push("/dashboard")
        });
    }

    return (
        <form method="POST">

          <input type="text" placeholder="Enter Email" name="email" id="email" value={mail} onChange={(e) => setMail(e.target.value)} required />
        
          <input type="password" placeholder="Enter Password" name="psw" id="psw" value={password} onChange={(e) => setPassword(e.target.value)} required />
      
          <button onClick={handleSubmit} type="button">Login</button>
      </form>
    )
}