'use client'
  import { useState } from 'react'
  import { testConnection } from '@/lib/api'
  
  export default function TestPage() {
    const [result, setResult] = useState(null)
    
    const handleTest = async () => {
      const data = await testConnection()
      setResult(data)
    }
    
    return (
      <div className="p-8">
        <button onClick={handleTest}>Test Connection</button>
        {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
      </div>
    )
  }