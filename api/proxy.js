export default async function handler(req, res) {
  // بنسمح للموقع بتاعنا بس إنه يكلم الـ API
  res.setHeader("Access-Control-Allow-Origin", "*");
  if (req.method !== "POST") return res.status(405).json({ error: "Method not allowed" });

  const { url } = req.body;
  if (!url) return res.status(400).json({ error: "Missing URL" });

  const API_KEY = "cf303b84c71f2c87aab20c3720acee62"; // ⚠️ حط المفتاح هنا
  const API_URL = "https://peakerr.com/api/v2";

  try {
    const formData = new URLSearchParams();
    formData.append('key', API_KEY);
    formData.append('action', 'add');
    formData.append('service', '31859');
    formData.append('link', url);
    formData.append('quantity', '1000');

    // Vercel هو اللي هيكلم Peakerr دلوقتي (Server-to-Server)
    const peakerrRes = await fetch(API_URL, {
      method: 'POST',
      body: formData
    });

    const text = await peakerrRes.text();
    let data;
    try {
      data = JSON.parse(text);
    } catch(e) {
      return res.status(200).json({ error: "Invalid response from Peakerr: " + text });
    }

    res.status(200).json(data);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
}
