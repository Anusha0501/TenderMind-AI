import "./globals.css";
export const metadata = { title: "TenderMind-AI", description: "AI tender monitoring and qualification platform" };
export default function RootLayout({ children }: { children: React.ReactNode }) { return <html lang="en" className="dark"><body>{children}</body></html>; }
