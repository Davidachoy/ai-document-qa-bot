export async function testConnection() {
    const response = await fetch('/api/test', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ test: 'hello from nextjs' }),
    })
    return response.json()
  }