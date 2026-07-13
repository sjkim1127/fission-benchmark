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
  title: {
    default: "Fission Benchmark",
    template: "%s · Fission Benchmark",
  },
  description:
    "Multi-decompiler semantic quality and Fission↔Ghidra layered parity (shared p-code-class IR).",
  openGraph: {
    title: "Fission Benchmark",
    description:
      "Semantic multi-decompiler ranking + dedicated Fission vs Ghidra IR parity.",
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
