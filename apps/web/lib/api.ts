export type Tender = { id: number; source: string; external_ref: string; title: string; buyer_name: string; category: string; location: string; estimated_value: number | null; closes_at: string; status: string };
const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";
export async function getTenders(): Promise<Tender[]> {
  const response = await fetch(`${API_URL}/api/v1/tenders`, { next: { revalidate: 30 } });
  if (!response.ok) return [];
  return response.json();
}
