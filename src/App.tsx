import React, { useState } from 'react';
import Editor from '@monaco-editor/react';

function App() {
  const [code, setCode] = useState('# Write your Python code here\nname = input("Enter your name: ")\nprint("Hello", name)');
  const [input, setInput] = useState('');
  const [output, setOutput] = useState('');
  const [loading, setLoading] = useState(false);

  const runCode = async () => {
    setLoading(true);
    try {
      const response = await fetch('https://code-runner-backend-gtwu.onrender.com/run', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code, input }),
      });
      const data = await response.json();
      setOutput(data.output || data.error || 'No output');
    } catch {
      setOutput('❌ Error connecting to backend.');
    }
    setLoading(false);
  };

  return (
    <div style={{ height: '100vh', display: 'flex', flexDirection: 'column' }}>
      <h2 style={{ textAlign: 'center', background: '#1e1e1e', color: '#fff', margin: 0, padding: '10px' }}>
        🧠 Python Code Editor for Kids
      </h2>
      <Editor
        height="45vh"
        defaultLanguage="python"
        value={code}
        theme="vs-dark"
        onChange={(value) => setCode(value || '')}
      />
      <textarea
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Enter input for your program"
        style={{ width: '100%', height: '10vh', padding: '10px', fontFamily: 'monospace', fontSize: '16px' }}
      />
      <div style={{ padding: '10px' }}>
        <button onClick={runCode} style={{ padding: '8px 20px', fontSize: '16px' }}>
          {loading ? 'Running...' : 'Run Code'}
        </button>
      </div>
      <pre style={{ background: '#000', color: '#0f0', padding: '10px', margin: '10px', height: '20vh', overflow: 'auto' }}>
        {output || 'Output will appear here...'}
      </pre>
    </div>
  );
}

export default App;
