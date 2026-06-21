import type { Config } from "tailwindcss";
const config: Config = { darkMode: "class", content: ["./app/**/*.{ts,tsx}", "./components/**/*.{ts,tsx}"], theme: { extend: { colors: { ink: "#080b12", panel: "#101522", accent: "#7c3aed" }, boxShadow: { glow: "0 0 80px rgba(124,58,237,.24)" } } }, plugins: [] };
export default config;
