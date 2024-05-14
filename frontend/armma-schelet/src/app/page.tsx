import Image from "next/image";
import styles from "./page.module.css";
import { permanentRedirect } from 'next/navigation'

export default function HomePage() {
  permanentRedirect('/login')
}
