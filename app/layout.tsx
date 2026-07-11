import type { Metadata } from "next";
import { Inter, JetBrains_Mono } from "next/font/google";
import "./globals.css";

const inter = Inter({
  subsets: ["latin"],
  variable: "--font-inter",
  display: "swap",
});

const jetbrainsMono = JetBrains_Mono({
  subsets: ["latin"],
  variable: "--font-mono",
  display: "swap",
});

export const metadata: Metadata = {
  title: "Fission Benchmark Dashboard",
  description:
    "Multi-decompiler comparison benchmark: Fission vs Ghidra, angr, RetDec, Radare2, Snowman, rev.ng, Reko",
  openGraph: {
    title: "Fission Benchmark Dashboard",
    description: "Live benchmark results comparing Fission against leading open-source decompilers",
    type: "website",
  },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={`${inter.variable} ${jetbrainsMono.variable}`}>
      <body style={{ fontFamily: "var(--font-inter, system-ui, sans-serif)" }}>
        {children}
      </body>
    </html>
  );
}
