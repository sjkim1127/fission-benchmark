import { revalidatePath } from "next/cache";
import { NextRequest, NextResponse } from "next/server";

// Invalidates the ISR page cache for "/".
// Called by GitHub Actions after an official benchmark run publishes results.
export async function POST(request: NextRequest) {
  const authorization = request.headers.get("authorization");
  const secret = process.env.REVALIDATE_SECRET;

  if (!secret) {
    return NextResponse.json({ error: "REVALIDATE_SECRET not configured" }, { status: 500 });
  }

  if (authorization !== `Bearer ${secret}`) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  // Revalidate the root page so the next request fetches fresh benchmark data.
  revalidatePath("/");

  return NextResponse.json({
    revalidated: true,
    timestamp: new Date().toISOString(),
  });
}
