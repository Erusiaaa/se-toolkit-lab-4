import { useState, useEffect } from 'react'

function App() {
  const [items, setItems] = useState([])
  const [token, setToken] = useState('my-secret-api-key')

  useEffect(() => {
    fetch('http://10.93.25.146:42002/items/', {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })
      .then(res => res.json())
      .then(data => {
        console.log('Data:', data)
        setItems(data)
      })
      .catch(err => console.error('Error:', err))
  }, [])

  return (
    <div>
      <h1>Items</h1>
      <pre>{JSON.stringify(items, null, 2)}</pre>
    </div>
  )
}

export default App