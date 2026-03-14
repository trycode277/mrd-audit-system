import React, { useState } from "react";
import UploadForm from "./components/UploadForm";
import AuditResult from "./components/AuditResult";

function App() {

  const [result, setResult] = useState(null);

  return (
    <div style={{padding:"40px"}}>

      <h1>AI Medical Record Audit Agent</h1>

      <UploadForm setResult={setResult} />

      <AuditResult result={result} />

    </div>
  );
}

export default App;